"""
Paul Deater
SDEV245
Final
10/16/2026
Application builds a simple CLI taking a file or a directory checking them with regex to find secret patterns if they exist
"""

import argparse
import re
import sys
from pathlib import Path

#Regexs are implemented using the Id, the name, and the regex
REGEX_PATTERNS = [
    (
        "private-key-block",
        "Secret access key (keyword-gated)",
        re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP |ENCRYPTED )?PRIVATE KEY-----"),
        0,
    ),
    (
        "aws-secret-access-key",
        "Secret access key (keyword-gated)",
        re.compile(r"b(?:A3T[A-Z0-9]|AKIA|ASIA|ABIA|ACCA)[A-Z2-7]{16}b"),
        0,
    ),
    (
        "google-api-key",
        "API key",
        re.compile(r"bAIza[0-9A-Za-z_-]{35}b"),
        0,
    ),
    (
        "instagram-access-token",
        "Access token",
        re.compile(r"bIGQ[0-9A-Za-z_-]{100,}"),
        0,
    ),
    (
        "square-access-token",
        "Production access token",
        re.compile(r"bEAAA[0-9A-Za-z_-]{60}b"),
        0,
    )
]

# scans file for secret patterns adding them to a list if found
def Scan_File (Path, Root):
    Found_Secrets = []

    Content = Path.read_text(encoding="utf-8", errors="replace")

    try:
        Display_Path = str(Path.relative_to(Root))
    except ValueError:
        Display_Path = str(Path)

    for Line_Number, Line in enumerate(Content.splitlines(), start=1):
            for Rule_Id, Description, Pattern, Group in REGEX_PATTERNS:
                for Match in Pattern.finditer(Line):
                    Secret = Match.group(Group)
    
                    Found_Secrets.append({
                        "file": Display_Path,
                        "line": Line_Number,
                        "rule": Rule_Id,
                        "description": Description,
                        "match": (Secret),
                    })
    return Found_Secrets

# Checks wether a file or directory has been input then calls the Scan-File function
def Evaluate_Input (Target: Path):
    Secrets_found = []

    if not Target.exists():
        raise FileNotFoundError(f"Path does not exist: {Target}")

    if Target.is_dir():
        Root = Target
    else:
        Root = Target.parent

    if Target.is_file():
        Location = [Target]
    elif Target.is_dir():
        Location = sorted(p for p in Target.rglob("*") if p.is_file())
    else:
        raise ValueError(f"Not a regular file or directory: {Target}")
    
    for Path in Location:
        Secrets_found.extend(Scan_File(Path, Root))

    return Secrets_found
    

def main():
    # Creates the cli
    parser = argparse.ArgumentParser(description = "Scans an input file of directory for hardcoded secrets")

    parser.add_argument(
        "path",
        type = Path,
        help = "Scan file or directory"
    )

    args = parser.parse_args()

    try:
        Findings = Evaluate_Input(args.path.resolve())
    except:
        raise ("Error")

    # Outputs the result of the search
    if not Findings:
        print("No potential hardcoded secrets found.")
    else:
        print(f"Found {len(Findings)} potential secret(s):\n")
        for item in Findings:
            print(
                f"[{item['rule']}] "
                f"{item['file']}:Line {item['line']}"
            )
            print(f"  {item['description']}: {item['match']}")


if __name__ == "__main__":
    main()