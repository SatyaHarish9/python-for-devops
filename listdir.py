import os
pathlist = input("Enter the path: ")
#print(pathlist)
arr = os.listdir(pathlist)
print(arr)