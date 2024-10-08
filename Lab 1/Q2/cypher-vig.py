# Encrypt the message "the house is being sold tonight" using one of the 
# following ciphers. Ignore the space between words. Decrypt the message to 
# get the original plaintext:
# b) Autokey cipher with key = 7
def encrypt_data(text, key):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    text=text.replace(' ', '')
    key=(key*(len(text) // len(key)+1))[:len(text)]
    ciphertext=''
    for i in range(len(text)):
        if text[i] in alphabet:
            index = (alphabet.index(text[i]) + alphabet.index(key[i])) % 26
            ciphertext+=alphabet[index]
        else: 
            ciphertext+=text[i]
    return ciphertext

def decrypt_data(text,key):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    text=text.replace(' ', '')
    key=(key*(len(text) // len(key) + 1)) [:len(text)]
    plaintext=''
    for i in range(len(text)):
        if text[i] in alphabet:
            index =(alphabet.index(text[i]) - alphabet.index(key[i])) % 26 
            plaintext+=alphabet[index]
        else:
            plaintext+=text[i]
    return plaintext

message1=input("Enter the message to be encrypted : ")
key1=input("Enter the key message : ")
encrypted_message=encrypt_data(message1,key1)
print(f'Encrypted Message (Vigenere) : {encrypted_message}')

message2=input("Enter the message to be decrypted : ")
key2=input("Enter the key message : ")
decrypted_message=decrypt_data(message2,key2)
print(f'Decrypted Message (Vigenere) : {decrypted_message}')
