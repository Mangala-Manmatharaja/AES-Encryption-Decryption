# AES Encryption-Decryption using Python & Galois Field

This project implements **128-bit AES encryption and decryption** using Python and the [`galois`](https://pypi.org/project/galois/) library for Galois Field arithmetic. It is developed as part of a coursework project in **Cryptography and Network Security**.

## 🔐 Features

- AES-128 encryption (10 rounds)
- Key expansion and round key generation
- Byte substitution using S-Boxes
- Shift Rows and Mix Columns transformations
- Full encryption and decryption cycles
- Custom implementation using NumPy and Galois fields
- No reliance on high-level cryptographic libraries

## 📌 Requirements

- Python 3.7+
- numpy
- galois (for finite field operations)

### 🔧 Installation
  bash
      
      pip install numpy galois

---
## 🚀 Usage
To encrypt or decrypt a 128-bit (4x4 byte) matrix:

    import numpy as np
    from aes_encryption import encrypt, decrypt

      # Example 4x4 byte matrix (plaintext and key)
        plaintext = np.array([
        [0x32, 0x88, 0x31, 0xe0],
        [0x43, 0x5a, 0x31, 0x37],
        [0xf6, 0x30, 0x98, 0x07],
        [0xa8, 0x8d, 0xa2, 0x34]
        ], dtype=np.uint8)

        key = np.array([
        [0x2b, 0x28, 0xab, 0x09],
        [0x7e, 0xae, 0xf7, 0xcf],
        [0x15, 0xd2, 0x15, 0x4f],
        [0x16, 0xa6, 0x88, 0x3c]
        ], dtype=np.uint8)

      ciphertext = encrypt(plaintext, key)
      decrypted = decrypt(ciphertext, key)

## 🧠 Learning Outcomes
-  Understanding of symmetric encryption and AES internals
-  Practical application of Galois Field math in cryptography
-  Manual implementation of cryptographic steps (S-Box, shift rows, mix columns)



