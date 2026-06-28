import os

path = "."  # current directory, change if needed

contents = os.listdir(path)

print(f"Contents of '{path}':")
for item in contents:
    print(item)