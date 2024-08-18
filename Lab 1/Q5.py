# the type of attack is known plain-text attack
def shift_cipher(text,shift):
  result = ""
  for char in text:
    if char.isalpha():
      base = ord('A') if char.isupper() else ord('a')
      shifted_char = chr((ord(char) - base +shift) % 26 + base)
      result+=shifted_char
    else:
      result+=char
  return result
def find_shift(plaintext,ciphertext):
  if len(plaintext)!=len(ciphertext):
    raise ValueError("Plaintext and ciphertext lengths must be equal")
  
  shift=(ord(ciphertext[0].upper())-ord(plaintext[0].upper()))%26
  return shift

ciphertext1="CIW"
plaintext1="yes"
ciphertext2="XVIEWYWI"
shift=find_shift(plaintext1,ciphertext1)
plaintext2=shift_cipher(ciphertext2,-shift)
print("Attack type: Known-plaintext attack")
print("Plaintext for 'XVIEWYWUI' :",plaintext2)
