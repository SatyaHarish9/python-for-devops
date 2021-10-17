import os.path
from os import path

def main():
    print("File exists: "+str(path.exists('send-email.py')))
    print("File exists: " + str(path.exists('send-no-email.py')))
    print("directort exists: " + str(path.exists('myDirectory')))

if __name__ == "__main__":
    main()