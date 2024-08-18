from string import ascii_uppercase

# Function to compute modular inverse
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Function to decrypt using affine cipher
def affine_decrypt(ciphertext, a, b):
    m = 26
    a_inv = mod_inverse(a, m)
    if a_inv is None:
        return None
    
    plaintext = ""
    for char in ciphertext:
        if char in ascii_uppercase:
            y = ord(char) - ord('A')
            x = (a_inv * (y - b)) % m
            plaintext += chr(x + ord('A'))
        else:
            plaintext += char
    return plaintext

# Known plaintext-ciphertext pair
plaintext_known = "AB"
ciphertext_known = "GL"

# Given ciphertext to decrypt
ciphertext = "XPALASXYFGFUKPXUSOGEUTKCDGEXANMGNVS"

# Possible values for 'a' (must be coprime with 26)
valid_a_values = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

# Brute-force search for the key
for a in valid_a_values:
    for b in range(26):
        decrypted_text = affine_decrypt(ciphertext_known, a, b)
        if decrypted_text == plaintext_known:
            print(f"Possible key found: a = {a}, b = {b}")
            print("Decrypted message:")
            print(affine_decrypt(ciphertext, a, b))
            break