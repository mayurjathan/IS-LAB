# Use the Playfair cipher to encipher the message "The key is hidden under the 
# door pad". The secret key can be made by filling the first and part of the second 
# row with the word "GUIDANCE" and filling the rest of the matrix with the 
# rest of the alphabet.
import string 

def generate_playfair_matrix(key):
    key=''.join(sorted(set(key),key=key.index))
    alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix=[]
    for char in key.upper():
        if char not in matrix and char in alphabet:
            matrix.append(char)
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    return [matrix[i:i+5] for i in range(0,25,5)]

def preprocess_message(message):
    message=''.join(filter(str.isalpha,message)).upper()
    message=message.replace('J','I')
    digraphs=[]
    i=0
    while i < len(message):
        a=message[i]
        b=message[i+1] if i+1 <len(message) else 'X'
        if(a==b):
            digraphs.append(a + 'X')
            i+=1
        else:
            digraphs.append(a + b)
            i+=2

    if len(digraphs[-1]) == 1:
        digraphs[-1] += 'X'

    return digraphs

def find_position(char,matrix):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def playfair_encrypt(message,matrix):
     digraphs=preprocess_message(message)
     encrypted_message=[]
     for digraph in digraphs:
         a, b =digraph
         row_a,col_a=find_position(a,matrix)
         row_b,col_b=find_position(b,matrix)
         if row_a==row_b:
             encrypted_message.append(matrix[row_a][(col_a+1)%5])
             encrypted_message.append(matrix[row_b][(col_b+1)%5])
         elif col_a == col_b:
             encrypted_message.append(matrix[(row_a+1)%5][col_a])
             encrypted_message.append(matrix[(row_b+1)%5][col_b])
         else:
             encrypted_message.append(matrix[row_a][col_b])
             encrypted_message.append(matrix[row_b][col_a])
     return ''.join(encrypted_message)
key=input("Enter the key : ")
message=input("Enter the key to be encrypted : ")
matrix=generate_playfair_matrix(key)
encrypted_message=playfair_encrypt(message,matrix)
print("Playfair Matrix : ")
for row in matrix:
    print(' '.join(row))
print("\nEncrypted Message: ")
print(encrypted_message)

