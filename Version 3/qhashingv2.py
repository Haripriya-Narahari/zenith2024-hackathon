from hashlib import sha256
import numpy as np

def hash_string_to_angles(input_string):
    # Step 1: Hash the input string using SHA-256
    hashed_value = sha256(input_string.encode()).digest()
    
    # Step 2: Normalize the hash value to [0, 1]
    normalized_value = int.from_bytes(hashed_value, byteorder='big') / (2**256 - 1)
    
    # Step 3: Quantum Angle Embedding
    angle_embedding = round(2 * np.arcsin(np.sqrt(normalized_value)), 20)
    
    return angle_embedding

print(hash_string_to_angles("Hello World"))
print(hash_string_to_angles("Hello Worldi"))