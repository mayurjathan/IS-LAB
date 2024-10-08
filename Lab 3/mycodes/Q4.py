# Design and implement a secure file transfer system using RSA (2048-bit) and 
# ECC (secp256r1 curve) public key algorithms. Generate and exchange keys, then 
# encrypt and decrypt files of varying sizes (e.g., 1 MB, 10 MB) using both 
# algorithms. Measure and compare the performance in terms of key generation 
# time, encryption/decryption speed, and computational overhead. Evaluate the 
# security and efficiency of each algorithm in the context of file transfer, 
# considering factors such as key size, storage requirements, and resistance to 
# known attacks. Document your findings, including performance metrics and a 
# summary of the strengths and weaknesses of RSA and ECC for secure file 
# transfer.
from cryptography.hazmat.primitives.asymmetric import rsa, ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import time

# RSA Key Generation
start_time = time.time()
rsa_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
rsa_public_key = rsa_private_key.public_key()
rsa_key_gen_time = time.time() - start_time

# ECC Key Generation
start_time = time.time()
ecc_private_key = ec.generate_private_key(
    ec.SECP256R1(),
    default_backend()
)
ecc_public_key = ecc_private_key.public_key()
ecc_key_gen_time = time.time() - start_time

print(f"RSA Key Generation Time: {rsa_key_gen_time:.4f} seconds")
print(f"ECC Key Generation Time: {ecc_key_gen_time:.4f} seconds")


#RSA Encryption/Decryption

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

# Generate AES symmetric key for file encryption
aes_key = os.urandom(32)
iv = os.urandom(16)

# RSA Encryption of AES Key
start_time = time.time()
encrypted_aes_key = rsa_public_key.encrypt(
    aes_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
rsa_encrypt_time = time.time() - start_time


# Encrypt File using AES
def encrypt_file(file_path, aes_key, iv):
    with open(file_path, 'rb') as f:
        plaintext = f.read()

    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    with open(file_path + ".enc", 'wb') as f:
        f.write(iv + ciphertext)


# Decrypt AES Key using RSA
start_time = time.time()
decrypted_aes_key = rsa_private_key.decrypt(
    encrypted_aes_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
rsa_decrypt_time = time.time() - start_time


# Decrypt File using AES
def decrypt_file(encrypted_file_path, aes_key):
    with open(encrypted_file_path, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()

    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    with open(encrypted_file_path.replace(".enc", ".dec"), 'wb') as f:
        f.write(plaintext)


#ECC Encryption/Decryption

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# ECC Shared Secret
start_time = time.time()
shared_key = ecc_private_key.exchange(ec.ECDH(), ecc_public_key)
ecc_shared_key_time = time.time() - start_time

# Derive AES Key using KDF
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=os.urandom(16),
    iterations=100000,
    backend=default_backend()
)
symmetric_key = kdf.derive(shared_key)

# Encrypt File using AES (as before)
encrypt_file('example.txt', symmetric_key, iv)

# Decrypt File using AES (as before)
decrypt_file('example.txt.enc', symmetric_key)

print(f"RSA Encryption Time: {rsa_encrypt_time:.4f} seconds")
print(f"RSA Decryption Time: {rsa_decrypt_time:.4f} seconds")
print(f"ECC Shared Key Generation Time: {ecc_shared_key_time:.4f} seconds")