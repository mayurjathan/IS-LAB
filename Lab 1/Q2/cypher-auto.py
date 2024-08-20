def autokey_encrypt(plaintext, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    plaintext = plaintext.replace(' ', '')  # Remove spaces
    ciphertext = ''
    extended_key = [key] + [alphabet.index(char) for char in plaintext]
    for i in range(len(plaintext)):
        if plaintext[i] in alphabet:
            index = (alphabet.index(plaintext[i]) + extended_key[i]) % 26
            ciphertext += alphabet[index]
        else:
            ciphertext += plaintext[i]
    return ciphertext

def autokey_decrypt(ciphertext, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    plaintext = ''
    extended_key = [key]
    for i in range(len(ciphertext)):
        if ciphertext[i] in alphabet:
            index = (alphabet.index(ciphertext[i]) - extended_key[i]) % 26
            plaintext += alphabet[index]
            extended_key.append(alphabet.index(alphabet[index]))
        else:
            plaintext += ciphertext[i]
    return plaintext

message1=input("Enter the message to be encrypted : ")
key1=int(input("Enter the key value : "))
encrypted_message=autokey_encrypt(message1,key1)
print(f'Encrypted Message (Autokey) : {encrypted_message}')

message2=input("Enter the message to be decrypted : ")
key2=int(input("Enter the key message : "))
decrypted_message=autokey_decrypt(message2,key2)
print(f'Decrypted Message (Autokey) : {decrypted_message}')
