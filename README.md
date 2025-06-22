# AES Encryption-Decryption using Python & Galois Field

This project demonstrates simple XOR-based encryption and decryption using 128-bit (4x4 byte) matrices. It is implemented using Python and NumPy, primarily for educational purposes in understanding symmetric key operations at the byte lev.

## 🔐 Features

- 4x4 byte matrix-based XOR encryption
- XOR is used for both encryption and decryption (symmetry property)
- Demonstrates transformation of plaintext to ciphertext and back
- Easy-to-follow code using NumPy for array manipulation

## 📌 Requirements

- Python 3.7+
- numpy

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

## 🛡️ Disclaimer
- This implementation is for educational use only and is not secure for real-world applications. XOR encryption with static keys is vulnerable to many attacks.

## 👤 Author
- Mangala-Manmatharaja

