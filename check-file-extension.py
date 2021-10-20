# Python program to find a file with particular extension.
import os
import datetime

for dirpath, dirname, filename in os.walk('/Users/sgumpall/Documents/nutanix'):
    for file in filename:
        complete_path = os.path.join(dirpath,file)
        if file.endswith(".conf"):
            print(complete_path)
            file_size = os.path.getsize(complete_path)
            print("File size is: ", file_size, "bytes")
        else:
            print("No file with .conf exists")