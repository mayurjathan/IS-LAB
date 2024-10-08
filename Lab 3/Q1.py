# Using RSA, encrypt the message "Asymmetric Encryption" with the public key 
# (n, e). Then decrypt the ciphertext with the private key (n, d) to verify the original 
# message.

# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_OAEP
# from binascii import hexlify, unhexlify


# # Function to generate RSA keys
# def generate_rsa_keys():
#     key = RSA.generate(2048)
#     private_key = key.export_key()
#     public_key = key.publickey().export_key()
#     return key, private_key, public_key


# # Function to encrypt the message using RSA public key
# def rsa_encrypt(plain_text, public_key):
#     rsa_key = RSA.import_key(public_key)
#     cipher = PKCS1_OAEP.new(rsa_key)
#     cipher_text = cipher.encrypt(plain_text.encode())
#     return hexlify(cipher_text).decode()


# # Function to decrypt the ciphertext using RSA private key
# def rsa_decrypt(cipher_text, private_key):
#     rsa_key = RSA.import_key(private_key)
#     cipher = PKCS1_OAEP.new(rsa_key)
#     decrypted_text = cipher.decrypt(unhexlify(cipher_text))
#     return decrypted_text.decode()


# # Generate RSA keys
# key, private_key, public_key = generate_rsa_keys()

# # Message to encrypt
# plain_text = "Asymmetric Encryption"

# # Encrypt the message using the public key
# cipher_text = rsa_encrypt(plain_text, public_key)
# print(f"Ciphertext: {cipher_text}")

# # Decrypt the ciphertext using the private key
# decrypted_text = rsa_decrypt(cipher_text, private_key)
# print(f"Decrypted text: {decrypted_text}")

# # Verify if the original message is recovered
# assert decrypted_text == plain_text

from Crypto.PublicKey import RSA  # Import RSA key generation from PyCryptodome
from Crypto.Cipher import PKCS1_OAEP  # Import the PKCS#1 OAEP cipher for RSA
import binascii  # Import binascii for hexadecimal conversions

# Generate a new RSA key pair with a key size of 2048 bits
key = RSA.generate(2048)  # Create a new RSA key object

# Extract the components of the key
n = key.n  # The modulus
e = key.e  # The public exponent
d = key.d  # The private exponent

# Get the public key for encryption
public_key = key.publickey()  # Extract the public key from the key object
private_key = key  # Store the private key for later decryption

# Print the key components
print(f"n={n}")  # Print the modulus
print(f"e={e}")  # Print the public exponent
print(f"d={d}")  # Print the private exponent

# Message to be encrypted
message = "Asymmetric Encryption"  # Define the plaintext message to encrypt

# Encrypt the message using the public key

# Initialize the cipher for encryption with the public key
cipher_encrypt = PKCS1_OAEP.new(public_key) 

# Encrypt the message (convert to bytes)
ciphertext = cipher_encrypt.encrypt(message.encode())  #.encode() converts the message to bytes

# Print the encrypted message in hexadecimal format
print("Ciphertext (hex):", binascii.hexlify(ciphertext).decode())  


# Decrypt the ciphertext using the private key

# Initialize the cipher for decryption with the private key
cipher_decrypt = PKCS1_OAEP.new(private_key)  

# Decrypt the ciphertext to get the original message
decrypted_message = cipher_decrypt.decrypt(ciphertext)  

# Display the decrypted message
print("Decrypted message:", decrypted_message.decode())  # Print the original message after decryption