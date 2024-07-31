def encrypt_additive(plaintext, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    plaintext = plaintext.replace(' ', '')  
    ciphertext = ''
    for char in plaintext:
        if char in alphabet:
            index = (alphabet.index(char) + key) % 26
            ciphertext += alphabet[index]
        else:
            ciphertext += char
    return ciphertext

def decrypt_additive(ciphertext, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ciphertext  = ciphertext.replace(' ', '')
    plaintext = ''
    for char in ciphertext:
        if char in alphabet:
            index = (alphabet.index(char) - key) % 26
            plaintext += alphabet[index]
        else:
            plaintext += char
    return plaintext

message1 = input("Enter the message to be encrypted: ")
key1 = int(input("Enter the key value :"))
encrypted_message = encrypt_additive(message1, key1)
print(f'Encrypted Message: {encrypted_message}')

message2 = input("Enter the message to be decrypted: ")
key2 = int(input("Enter the key value :"))
decrypted_message = decrypt_additive(message2, key2)
print(f'Decrypted Message: {decrypted_message}')
