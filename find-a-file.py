# Program to search for a file.

# os.walk() returns the tuple where the first value is directory path, second is directory name(returns sub directories in the directory) and third is file name which returns all files in the directory and the sub-directories.

# argparse modules can be used to provide arguements to the python code. Here, we are providing the directory and file to search for at the run time. 

# Importing the os and argparse libraries.
import os
import argparse

my_parser = argparse.ArgumentParser(description='Reading the directory path to find the file')

my_parser.add_argument("pathname",help='Please enter the directory path')
my_parser.add_argument("filesearch",help='Please enter the filename to search')

args = my_parser.parse_args() 

for dirpath, dirname, filename in os.walk(args.pathname):
    for file in filename:
        if file == args.filesearch:
            print(os.path.join(dirpath,file))
      