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

```bash
pip install numpy galois

