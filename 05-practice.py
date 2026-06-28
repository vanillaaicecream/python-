# Program to print contents of a directory using os module
# Author: Vipul
# Date: 28-06-2026

import os  # importing the os module

"""
This program uses os.listdir() to fetch
all files and folders in a given directory
and prints them one by one.
"""

# ----- Set Directory Path -----
path = "."  # '.' means current directory

# Fetch all contents of the directory
contents = os.listdir(path)  # returns a list of filenames

# ----- Display Results -----
print(f"Contents of '{path}':")  # header

for item in contents:
    print(item)  # print each file/folder name

# End of program