#  Encrypt the message "I am learning information security" using one of the 
# following ciphers. Ignore the space between words. Decrypt the message to 
# get the original plaintext:
# Multiplicative cipher with key = 15
def encrypt_affine(plaintext, key1, key2):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    plaintext = plaintext.replace(' ', '')
    ciphertext = ''
    for char in plaintext:
        if char in alphabet:
            index = (alphabet.index(char) * key1 + key2) % 26
            ciphertext += alphabet[index]
        else:
            ciphertext += char
    return ciphertext

def decrypt_affine(ciphertext, key1, key2):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ciphertext = ciphertext.replace(' ', '')
    plaintext = ''
    inv_key = pow(key1, -1, 26)
    for char in ciphertext:
        if char in alphabet:
            index = (alphabet.index(char) - key2) * inv_key % 26
            plaintext += alphabet[index]
        else:
            plaintext += char
    return plaintext

message1=input("Enter the message to be encrypted : ")
key1=int(input("Enter the first key value (multiplicative key) : "))
key2=int(input("Enter the second key value (additive key) : "))
encrypted_message = encrypt_affine(message1,key1,key2)
print(f'Encrypted Message : {encrypted_message}')

message2=input("Enter the message to be decrypted : ")
key3=int(input("Enter the first key value (multiplicative key) : "))
key4=int(input("Enter the second key value (additive key) : "))
decrypted_message=decrypt_affine(message2,key3,key4)
print(f'Decrypted Message : {decrypted_message}')
