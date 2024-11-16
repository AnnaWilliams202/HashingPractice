import os
import hashlib

# Function to read the entire content of a file
def read_file_content(filepath):
    with open(filepath, "rb") as f:
        content = f.read()
        hashvalue = hashlib.sha256(content).hexdigest()
        return hashvalue


# Directory path containing files with potential duplicates
directory_path = "files"

# Dictionary to store file contents
hashes = {}

# Traverse through each file in the directory and its subdirectories
for root, dirs, files in os.walk(directory_path):
    for filename in files:
        filepath = os.path.join(root, filename)

        # Read the file content
        hashvalue = read_file_content(filepath)

        # Use the content as a key in the dictionary
        if hashvalue in hashes:
            print(f"Removing duplicate file: {filepath}")
            os.remove(filepath)
        else:
            hashes[hashvalue] = filepath