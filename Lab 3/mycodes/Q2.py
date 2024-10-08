from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os

# Generate ECC private and public keys
private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
public_key = private_key.public_key()

# Serialize public key to PEM format
pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Serialize private key to PEM format
pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

# Message to encrypt
message = input("Enter the message: ").encode()

# Derive a symmetric key from the private key
private_key_bytes = pem_private
backend = default_backend()
private_key = serialization.load_pem_private_key(private_key_bytes, password=None, backend=backend)
shared_key = private_key.exchange(ec.ECDH(), public_key)

# Derive a symmetric key for AES encryption
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=os.urandom(16),
    iterations=100000,
    backend=default_backend()
)
symmetric_key = kdf.derive(shared_key)

# Encrypt the message using AES
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(symmetric_key), modes.CFB(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(message) + encryptor.finalize()

print("Ciphertext:", ciphertext)

# Decrypt the message using the same symmetric key
cipher = Cipher(algorithms.AES(symmetric_key), modes.CFB(iv), backend=default_backend())
decryptor = cipher.decryptor()
decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()

print("Decrypted Message:", decrypted_message.decode())