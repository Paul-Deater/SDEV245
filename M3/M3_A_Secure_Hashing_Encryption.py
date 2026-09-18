"""
Paul Deater
SDEV245
Assignment - Secure Hashing and Encryption
9/17/2026
App asks for input from the user for text or a file to be hashed and then asks for another input which is encrypted and decrypted using a Caesar cipher.
"""

#1

import hashlib
import os

Hash_Input = input("Enter string or file to be hashed: ")

# Checks if the input is a file
if os.path.exists(Hash_Input):
    with open(Hash_Input, "rb") as File:
        Digest = hashlib.file_digest(File, "sha256")
        print(Digest.hexdigest())
#Otherwise it hashes the string
else:
    Hash_Al = hashlib.new("sha256")
    Hash_Al.update(Hash_Input.encode())

    print(Hash_Al.hexdigest())

#2

# The degree of shift
Cipher_Shift = 5

Cipher_Text = ""
Input_Data = input("Please enter text: ")

# Encryption function, loops through the string, checking for the type of character and ciphering it appropriately
def Caesar_Encrypt(Cipher_Text):
    for Character in Input_Data:

        if Character.isalpha():
            if Character.isupper():
                Cipher_Charcter_Code = ord(Character) + Cipher_Shift
                if Cipher_Charcter_Code > 90:
                    Cipher_Charcter_Code -= 26
                Cipher_Text += chr(Cipher_Charcter_Code)

            if Character.islower():
                Cipher_Charcter_Code = ord(Character) + Cipher_Shift
                if Cipher_Charcter_Code > 122:
                    Cipher_Charcter_Code -= 26
                Cipher_Text += chr(Cipher_Charcter_Code)
        else:
            Cipher_Text += Character

    print(Cipher_Text)
    return Cipher_Text

# Decryption function, loops through the string, checking for the type of character and deciphering it appropriately
def Caesar_Decrypt(Cipher_Encrypt_Text):
    Cipher_Decrypt_Text = ""
    for Character in Cipher_Encrypt_Text:

        if Character.isalpha():
            if Character.isupper():
                Cipher_Charcter_Code = ord(Character) - Cipher_Shift
                if Cipher_Charcter_Code > 90:
                    Cipher_Charcter_Code -= 26
                Cipher_Decrypt_Text += chr(Cipher_Charcter_Code)

            if Character.islower():
                Cipher_Charcter_Code = ord(Character) - Cipher_Shift
                if Cipher_Charcter_Code > 122:
                    Cipher_Charcter_Code -= 26
                Cipher_Decrypt_Text += chr(Cipher_Charcter_Code)
        else:
            Cipher_Decrypt_Text += Character

    print(Cipher_Decrypt_Text)

Cipher_Encrypt_Text = Caesar_Encrypt(Cipher_Text)
Caesar_Decrypt(Cipher_Encrypt_Text)