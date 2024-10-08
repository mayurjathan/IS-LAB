# Encrypt the message "Confidential Data" using DES with the following key: 
# "A1B2C3D4". Then decrypt the ciphertext to verify the original message.
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# Define the key and the message
key = input("Enter an 8-character key: ").encode()
message = input("Enter the message to encrypt: ")

# Create a DES cipher object
cipher = DES.new(key, DES.MODE_ECB)

# Encrypt the message
padded_message = pad(message.encode(), DES.block_size)
ciphertext = cipher.encrypt(padded_message)

# Decrypt the ciphertext
decrypted_padded_message = cipher.decrypt(ciphertext)
decrypted_message = unpad(decrypted_padded_message, DES.block_size).decode()

# Display results
print("Ciphertext (in hex):", ciphertext.hex())
print("Decrypted message:", decrypted_message)