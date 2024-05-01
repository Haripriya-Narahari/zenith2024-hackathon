from hashlib import sha256
import numpy as np
map_digit_to_char = {'0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'g','7':'h','8':'i','9':'j'}

def hash_string_to_angles(input_string):
    # Step 1: Hash the input string using SHA-256
    hashed_value = sha256(input_string.encode()).digest()
    
    # Step 2: Normalize the hash value to [0, 1]
    normalized_value = int.from_bytes(hashed_value, byteorder='big') / (2**256 - 1)
    
    # Step 3: Quantum Angle Embedding
    angle_embedding = round(2 * np.arcsin(np.sqrt(normalized_value)),12)
    angle = list(str(angle_embedding))
    
    angle.remove('.')
    print(angle)
    #angle = [map_digit_to_char[a] for a in angle]
    print(''.join(angle))
    hashed_value_1 = sha256(''.join(angle).encode()).hexdigest()
    return hashed_value_1

# Example usage
input_string = "a"
angle_embedding = hash_string_to_angles(input_string)
print("Hashed value:", angle_embedding)


input_string = "Hello World"
angle_embedding = hash_string_to_angles(input_string)
print("Hashed value:", angle_embedding)
