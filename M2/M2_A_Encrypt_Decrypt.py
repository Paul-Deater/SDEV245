"""
Paul Deater
SDEV245
Assignment - Encrypt/Decrypt Demo
9/10/2026
Program contains two functions that demonstrate basic symmetric and asymmetric encryption respectively using the Cryptography library
"""
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def Symmetric_Demo():
    print("***Symmetric_Demo***")

    #Key
    Key = Fernet.generate_key()
    print("Key:" , Key)

    Implement = Fernet(Key)

    #Message as bytes
    Message = b"Very secret symmetric message"
    print("Message:", Message)

    #Encrypt
    Message_Encrypted = Implement.encrypt(Message)
    print("Message Encrypted:", Message_Encrypted)

    #Decrypt
    print("Message Decrypted:", Implement.decrypt(Message_Encrypted))


def Asymmetric_Demo():
    print("\n***Asymmetric_Demo***")

    #Keys
    Private_Key = rsa.generate_private_key(public_exponent=65537, key_size=1024)
    print("Private Key:", Private_Key)

    Public_Key = Private_Key.public_key()
    print("Public Key:", Public_Key)

    #Message as bytes
    Message = b"Very secret asymmetric message"
    print("Message:", Message)

    #Encrypt
    Message_Encrypted = Public_Key.encrypt(Message, padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))
    print("Message Encrypted:", Message_Encrypted)

    #Decrypt
    print("Message Decrypted:", Private_Key.decrypt(Message_Encrypted, padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )))

Symmetric_Demo()

Asymmetric_Demo()