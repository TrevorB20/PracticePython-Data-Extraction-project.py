import os
import time

# Get to the current path of working directory
cwd = os.getcwd() 

# List all files of the current working directory
current_files = os.listdir(cwd)

# Create a list to store file information as dictionaries
Dictionaries_files = []

# Rehearse through all the files in the current working directory
for files in current_files:
    path = os.path.join(cwd, files)

    # Check to see if file is refering to an existing file and not a directory
    if os.path.isfile(path):
    
# Create a dictionary that includes the filename, size, and last modified time
        file_data = {
            'path': path,
            'size': os.path.getsize(path),
            'last_modified': time.ctime(os.path.getmtime(path))  # Get the last modified time
        }

        # Append to the list of dictionaries
        Dictionaries_files.append(file_data)

# Print list of dictionaries
for file_data in Dictionaries_files:
    print(file_data)
