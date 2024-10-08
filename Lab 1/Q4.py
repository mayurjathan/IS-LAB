# Use a Hill cipher to encipher the message "We live in an insecure world". Use 
# the following key:
# K = [03 03
# 02 07]

import math
def get_key_matrix(key):
  size=int(math.sqrt(len(key)))
  key_matrix=[[0] * size for _ in range(size)]
  k=0 
  for i in range(size):
    for j in range(size):
      key_matrix[i][j]=key[k]
      k+=1
  return key_matrix

def matrix_mult(A,B):
  size=len(A)
  result =[[0] * len(B[0]) for _ in range(size)]
  for i in range(size):
    for j in range(len(B[0])):
      for k in range(size):
        result[i][j] += A[i][k] * B[k][j]
      result[i][j]%=26
  return result

def hill_cipher(message,key):
  message=message.replace(" ","").upper()
  if len(message)%2!=0:
    message+="X"
  key_matrix=get_key_matrix(key)
  message_vector=[[ord(char)-65] for char in message]
  chunks = [message_vector[i:i+len(key_matrix)] for i in range(0, len(message_vector), len(key_matrix))]
  ciphertext = ""
  for chunk in chunks:
    result_vector = matrix_mult(key_matrix, chunk)
    ciphertext += ''.join(chr(result[0] + 65) for result in result_vector)
  return ciphertext
key = list(map(int, input("Enter the key as a list of 4 numbers (2x2 matrix): ").split()))
message = input("Enter the message to encrypt: ")
ciphertext = hill_cipher(message, key)
print("Ciphertext:", ciphertext)
  
 
