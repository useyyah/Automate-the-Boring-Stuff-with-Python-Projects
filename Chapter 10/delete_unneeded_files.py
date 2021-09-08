#! python3
# delete_unneeded_files.py - Walks through a directory and finds large files.

import os

while True:
    try:
        dir_search = input("Please type in a directory path to search.\n")
        os.chdir(dir_search)
        dir_search = os.path.abspath('.')
        print("Searching " + dir_search + '...')
        break
    except FileNotFoundError:
        print("Path not found. Please enter a complete path.")

for folder_name, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        filename = os.path.join(folder_name, filename)
        size = os.path.getsize(filename)
        if size > 100000000:
            print(os.path.abspath(filename) + ' - ' + str(size / 10**6) + 'MB')

print("Done.")