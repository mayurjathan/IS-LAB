from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Define the key and the message
key_input = input("Enter the key in hexadecimal format (32 characters): ")
key = bytes.fromhex(key_input)

message = input("Enter the message: ")

# Create an AES cipher object
cipher = AES.new(key, AES.MODE_ECB)

# Encrypt the message
padded_message = pad(message.encode(), AES.block_size)
ciphertext = cipher.encrypt(padded_message)

# Decrypt the ciphertext
decrypted_padded_message = cipher.decrypt(ciphertext)
decrypted_message = unpad(decrypted_padded_message, AES.block_size).decode()

# Display results
print("Ciphertext (in hex):", ciphertext.hex())
print("Decrypted message:", decrypted_message)