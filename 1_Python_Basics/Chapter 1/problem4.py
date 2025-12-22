# Write a python program to print the contents of a directory using the OS module. Search online for the function which does that. 

import os

directory_path= '/' # Specify the directory you want to list 
contents = os.listdir(directory_path)
for item in contents:
    print(item)