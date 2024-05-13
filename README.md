# Educational Ransomware Simulation

## Overview

This project is a simple simulation of ransomware and is intended purely for educational purposes. The objective of this simulation is to help students, educators, and cybersecurity enthusiasts understand how ransomware works and what measures can be taken to prevent such attacks. This project is not intended for real-world malicious use and should only be used in controlled, ethical, and legal environments.

## Description

The simulation consists of two main Python scripts:

1. **Encryption Script (`encrypt.py`)** - This script encrypts all `.txt` files in the directory where it's executed, using symmetric encryption (AES) provided by the `cryptography` library.
2. **Decryption Script (`decrypt.py`)** - This script decrypts all `.txt` files that were encrypted by the encryption script using the same key.

The encryption key is generated during the first run of the encryption script and is saved locally in a file named `key.key`. This key is crucial for the decryption process.

## How to Use

### Prerequisites

To run this project, you will need Python installed on your machine along with the `cryptography` package. You can install the required package using pip:

```bash
pip install cryptography
```
