import numpy as np

def xor_operation(matrix1, matrix2):
    return np.bitwise_xor(matrix1, matrix2)

def print_matrix(label, matrix):
    print(f"{label}")
    for row in matrix:
        print(" ".join(f"0x{val:02x}" for val in row))
    print()

# Key used
key = np.array([
    [0x0f, 0x47, 0x0c, 0xaf],
    [0x15, 0xd9, 0xb7, 0x7f],
    [0x71, 0xe8, 0xad, 0x67],
    [0xc9, 0x59, 0xd6, 0x98]
], dtype=np.uint8)

# PlainText 1 and 2
plain_text1 = np.array([
    [0x01, 0x23, 0x45, 0x67],
    [0x89, 0xab, 0xcd, 0xef],
    [0xfe, 0xdc, 0xba, 0x98],
    [0x76, 0x54, 0x32, 0x10]
], dtype=np.uint8)

plain_text2 = np.array([
    [0x01, 0x89, 0xfe, 0x76],
    [0x23, 0xab, 0xdc, 0x54],
    [0x45, 0xcd, 0xba, 0x32],
    [0x67, 0xef, 0x98, 0x10]
], dtype=np.uint8)

# Process for PlainText-1
cipher_text1 = xor_operation(plain_text1, key)
deciphered_text1 = xor_operation(cipher_text1, key)

# Process for PlainText-2
cipher_text2 = xor_operation(plain_text2, key)
deciphered_text2 = xor_operation(cipher_text2, key)

# Output
print_matrix("KEY USED", key)

print_matrix("PlainText-1", plain_text1)
print_matrix("CipherText-1", cipher_text1)
print_matrix("DecipheredText-1", deciphered_text1)

print_matrix("PlainText-2", plain_text2)
print_matrix("CipherText-2", cipher_text2)
print_matrix("DecipheredText-2", deciphered_text2)

# Optional validation
assert np.array_equal(deciphered_text1, plain_text1), "Decryption failed for PlainText-1"
assert np.array_equal(deciphered_text2, plain_text2), "Decryption failed for PlainText-2"
