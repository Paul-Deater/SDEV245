"""
Paul Deater
SDEV245
Midterm
9/18/2026
This App asks for user input, hashes and stores the information, encrypts and decrypts the input through AES, -
    then compares the hash of the decrypted information with the initial hash
"""
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, hmac

#Key generation
C_Key = os.urandom(32)
H_Key = os.urandom(32)
Iv = os.urandom(16)

#Acquiring input
User_Input = input("Please enter a message or file name:")

#Intial hash and storage
Hasher = hmac.HMAC(H_Key, hashes.SHA256())
Hasher.update(User_Input.encode()) 
Hash_Object = Hasher.finalize()

print("Input Hashed:", Hash_Object)

#Encryption
Short_Cipher = Cipher(algorithms.AES(C_Key), modes.CTR(Iv))

Ciph_Encryp = Short_Cipher.encryptor()

Encrypted_storage = Ciph_Encryp.update(User_Input.encode()) + Ciph_Encryp.finalize()

print("Encryption completed")

#Decryption
Ciph_Decryp = Short_Cipher.decryptor()

Decrypted_Data = Ciph_Decryp.update(Encrypted_storage) + Ciph_Decryp.finalize()

print("Decryption completed")


#Hash Verification
try:
    Hasher = hmac.HMAC(H_Key, hashes.SHA256())
    Hasher.update(Decrypted_Data) 
    Hasher.verify(Hash_Object)
    print("Verified: " + Decrypted_Data.decode())
except:
    print("Failed data does not match")

