from cryptography.fernet import Fernet
import os

# Open and read the encryption key from the 'key.key' file
with open("key.key", "rb") as f:
    key = f.read()
    
# Create a Fernet object for decryption using the read key
fernet = Fernet(key)

# Traverse through all directories and files in the current working directory
for folder in os.walk(os.getcwd()):
    for file in folder[2]:
        if str(file).endswith(".txt"):
            # Open the encrypted text file in binary read mode
            with open(str(file), "rb") as f:
                data = f.read()
            
            # Decrypt the data read from the file
            decrypted = fernet.decrypt(data)

            # Write the decrypted data back to the same file, overwriting it
            with open(str(file), "wb") as f:
                f.write(decrypted)


print("done")
