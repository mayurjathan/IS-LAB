import time
import random
from sympy import isprime, nextprime

# Function to generate a large prime number
def generate_large_prime(bits=512):
    p = random.getrandbits(bits)
    while not isprime(p):
        p = random.getrandbits(bits)
    return p

# Function to generate a private key
def generate_private_key(prime):
    return random.randint(1, prime - 1)

# Function to compute the public key
def compute_public_key(private_key, base, prime):
    return pow(base, private_key, prime)

# Function to compute the shared secret key
def compute_shared_secret(public_key, private_key, prime):
    return pow(public_key, private_key, prime)

# Set parameters
bits = 512  # Size of the prime number
base = 2    # Common base (generator)

# Generate a large prime number for the prime modulus
prime = generate_large_prime(bits)

# Generate private keys for two peers
private_key_peer1 = generate_private_key(prime)
private_key_peer2 = generate_private_key(prime)

# Compute public keys for two peers
start_time = time.time()
public_key_peer1 = compute_public_key(private_key_peer1, base, prime)
public_key_peer2 = compute_public_key(private_key_peer2, base, prime)
end_time = time.time()
print(f"Time taken for public key generation: {end_time - start_time:.5f} seconds")

# Compute shared secrets
start_time = time.time()
shared_secret_peer1 = compute_shared_secret(public_key_peer2, private_key_peer1, prime)
shared_secret_peer2 = compute_shared_secret(public_key_peer1, private_key_peer2, prime)
end_time = time.time()
print(f"Time taken for shared secret computation: {end_time - start_time:.5f} seconds")

# Print results
print(f"Prime: {prime}")
print(f"Base: {base}")
print(f"Private Key Peer 1: {private_key_peer1}")
print(f"Private Key Peer 2: {private_key_peer2}")
print(f"Public Key Peer 1: {public_key_peer1}")
print(f"Public Key Peer 2: {public_key_peer2}")
print(f"Shared Secret (Peer 1): {shared_secret_peer1}")
print(f"Shared Secret (Peer 2): {shared_secret_peer2}")

# Verify if both computed shared secrets match
if shared_secret_peer1 == shared_secret_peer2:
    print("Key exchange successful. Shared secrets match!")
else:
    print("Key exchange failed. Shared secrets do not match.")