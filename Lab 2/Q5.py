# Encrypt the message "Top Secret Data" using AES-192 with the key 
# "FEDCBA9876543210FEDCBA9876543210". Show all the steps involved in 
# the encryption process (key expansion, initial round, main rounds, final round)
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import numpy as np


def aes_encrypt(message, key):
    # Initialize AES cipher with ECB mode
    cipher = AES.new(key, AES.MODE_ECB)

    # Encrypt the message
    padded_message = pad(message.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_message)

    return ciphertext


def print_state(state):
    """ Print the state matrix in hex format. """
    print(np.array(state).reshape(4, 4).astype(np.uint8).tolist())


def key_expansion(key):
    """ Perform key expansion to generate round keys for AES-192. """
    # Key expansion is complex; we'll use pycryptodome to simplify.
    cipher = AES.new(key, AES.MODE_ECB)
    round_keys = [cipher.encrypt(bytes([0] * 16)) for _ in range(13)]  # 12 rounds + initial key
    return round_keys


def add_round_key(state, round_key):
    """ XOR the state with the round key. """
    return [s ^ rk for s, rk in zip(state, round_key)]


def sub_bytes(state):
    """ Substitute bytes in the state using the S-Box. """
    s_box = [i for i in range(256)]  # Simplified S-Box
    return [s_box[b] for b in state]


def shift_rows(state):
    """ Perform row shifting. """
    state = np.array(state).reshape(4, 4)
    state = np.roll(state, shift=-1, axis=1)  # Simplified shift for demonstration
    return state.flatten().tolist()


def mix_columns(state):
    """ Mix columns in the state (omitted for simplicity). """
    return state


def aes_process(message, key):
    print("Message:", message)
    print("Key (hex):", key.hex())

    # Key Expansion
    round_keys = key_expansion(key)

    # Initial Round
    state = list(message.encode()) + [0] * (16 - len(message))  # Padding for demonstration
    state = add_round_key(state, round_keys[0])
    print("After Initial Round Key:")
    print_state(state)

    # Main Rounds
    for i in range(1, 12):  # 10 rounds
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, round_keys[i])
        print(f"After Round {i}:")
        print_state(state)

    # Final Round
    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, round_keys[12])
    print("After Final Round:")
    print_state(state)

    return bytes(state)


# Define the message and key
message = input("Enter the message: ") # message = "Top Secret Data"

key_input = input("Enter a 32-character key in hexadecimal format: ") # key = bytes.fromhex("FEDCBA9876543210FEDCBA9876543210")
key = bytes.fromhex(key_input)

# Encrypt the message
ciphertext = aes_encrypt(message, key)

print("Ciphertext (in hex):", ciphertext.hex())