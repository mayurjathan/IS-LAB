# Compare the encryption and decryption times for DES and AES-256 for the 
# message "Performance Testing of Encryption Algorithms". Use a standard 
# implementation and report your findings.

import time
from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad, unpad

# Define the message
message = input("Enter the message: ")
message_bytes = message.encode()

# DES Key (8 bytes) and AES-256 Key (32 bytes)
des_key = b"8bytekey"  # 8 bytes for DES
aes_key = b"0123456789ABCDEF0123456789ABCDEF"  # 32 bytes for AES-256

# Padding the message
padded_message_des = pad(message_bytes, DES.block_size)
padded_message_aes = pad(message_bytes, AES.block_size)

# Number of iterations for averaging
iterations = 10000

# DES Encryption and Decryption
des_cipher = DES.new(des_key, DES.MODE_ECB)

start_time_des_encrypt = time.perf_counter()
for _ in range(iterations):
    des_ciphertext = des_cipher.encrypt(padded_message_des)
end_time_des_encrypt = time.perf_counter()

start_time_des_decrypt = time.perf_counter()
for _ in range(iterations):
    des_decrypted_message = unpad(des_cipher.decrypt(des_ciphertext), DES.block_size)
end_time_des_decrypt = time.perf_counter()

# AES-256 Encryption and Decryption
aes_cipher = AES.new(aes_key, AES.MODE_ECB)

start_time_aes_encrypt = time.perf_counter()
for _ in range(iterations):
    aes_ciphertext = aes_cipher.encrypt(padded_message_aes)
end_time_aes_encrypt = time.perf_counter()

start_time_aes_decrypt = time.perf_counter()
for _ in range(iterations):
    aes_decrypted_message = unpad(aes_cipher.decrypt(aes_ciphertext), AES.block_size)
end_time_aes_decrypt = time.perf_counter()

# Calculate average times per operation
des_encrypt_time = (end_time_des_encrypt - start_time_des_encrypt) / iterations
des_decrypt_time = (end_time_des_decrypt - start_time_des_decrypt) / iterations

aes_encrypt_time = (end_time_aes_encrypt - start_time_aes_encrypt) / iterations
aes_decrypt_time = (end_time_aes_decrypt - start_time_aes_decrypt) / iterations

# Results
print("DES Encryption Time (average):", des_encrypt_time)
print("DES Decryption Time (average):", des_decrypt_time)

print("AES-256 Encryption Time (average):", aes_encrypt_time)
print("AES-256 Decryption Time (average):", aes_decrypt_time)