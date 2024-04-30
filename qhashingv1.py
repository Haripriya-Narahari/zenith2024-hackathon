#Hashing - Version 1

#Simple Quantum Hashing using Angle Embedding
'''
Hashes the input string using the SHA-256 cryptographic hash function. SHA-256 produces a fixed-size output of 256 bits (32 bytes).
The hashed value is then normalized to be within the range [0, 1].

Using the normalized value, it calculates the angle embedding, which is a technique to represent information in a quantum state by mapping it to rotation angles.
Finally, it returns the angle embedding value.

'''

from hashlib import sha256
import numpy as np

def hash_string_to_angles(input_string):
    # Step 1: Hash the input string using SHA-256
    hashed_value = sha256(input_string.encode()).digest()

    # Step 2: Normalize the hash value to [0, 1]
    normalized_value = int.from_bytes(hashed_value, byteorder='big') / (2**256 - 1)

    # Step 3: Quantum Angle Embedding
    angle_embedding = 2 * np.arcsin(np.sqrt(normalized_value))

    return angle_embedding

# Example usage
input_string = "Hello"
angle_embedding = hash_string_to_angles(input_string)
print("Angle embedding value:", angle_embedding)
