from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Define the message
message = input("Enter the message: ")
message_bytes = message.encode()

# Define the 3DES key (24 bytes long)
key = get_random_bytes(24) # using the given key it gives an error so used get_random_bytes

# Create a Triple DES cipher object
cipher = DES3.new(key, DES3.MODE_ECB)

# Encrypt the message
padded_message = pad(message_bytes, DES3.block_size)
ciphertext = cipher.encrypt(padded_message)

# Decrypt the ciphertext
decrypted_padded_message = cipher.decrypt(ciphertext)
decrypted_message = unpad(decrypted_padded_message, DES3.block_size).decode()

# Display results
print("Ciphertext (in hex):", ciphertext.hex())
print("Decrypted message:", decrypted_message)