#!/usr/bin/python3
import os
import pathlib
import platform

# Discover current working directory
my_folder = pathlib.Path.cwd()
print(f"Current working directory: {my_folder}")

# Specify the target file we want to open
my_file = my_folder / 'example.txt'
print(f"Target file: {my_file}")

# Check if the file exists before trying to open it
if not my_file.exists():
    print(f"[-] File not found: {my_file}")
else:
    if platform.system() == "Windows":
        os.system(f"explorer \"{my_file}\"")
    elif platform.system() == "Darwin":  # macOS
        os.system(f"open \"{my_file}\"")
    else:  # Linux/Unix
        os.system(f"xdg-open \"{my_file}\"")
