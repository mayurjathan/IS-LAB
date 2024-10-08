# Implement the hash function in Python. Your function should start with
# an initial hash value of 5381 and for each character in the input string,
# multiply the current hash value by 33, add the ASCII value of the
# character, and use bitwise operations to ensure thorough mixing of the
# bits. Finally, ensure the hash value is kept within a 32-bit range by
# applying an appropriate mask.

def hash_function(input_string):
    """
    A simple hash function implementing the DJB2 algorithm.
    
    Args:
        input_string (str): The string to be hashed.

    Returns:
        int: The resulting hash value.
    """
    hash_value = 5381  # Initial hash value (starting point)

    # Iterate over each character in the input string
    for char in input_string:
        # Update the hash value using the current character's ASCII value
        # and the previous hash value
        hash_value = (hash_value * 33 + ord(char)) & 0xFFFFFFFF  # Keep it within 32 bits

    return hash_value  # Return the final hash value

# Example usage
input_string = "Hello, World!"  # The string to be hashed
hashed_value = hash_function(input_string)  # Compute the hash value
print(f"Hash value for '{input_string}' is: {hashed_value}")  # Print the result