#! python3
# selective_copy.py

import os, re, shutil

os.chdir(r'C:\Users\Ozgur2\Desktop')
print("Create a new folder on the desktop.")
new_folder = input("Which name do you want for your new folder? \n")
del_folder = 0

try:
    os.makedirs(new_folder)
except FileExistsError:
    print("This directory already exists.\n"
          "Your files will be placed in " + new_folder)
    del_folder += 1

new_file_path = os.path.abspath(new_folder)

while True:
    try:
        pull_directory = input("Where do you want to extract your files from.\n")
        os.chdir(pull_directory)
        path = os.getcwd()
        break
    except FileNotFoundError:
        print("Please type in a full path to the directory.")

type_of_file = input("What type of files do you want to copy?\n")
file_regex = re.compile(('.' + type_of_file + '$'), re.I)

i = 0
for folder_name, subfolders, filenames in os.walk(path):
    for filename in filenames:
        if file_regex.search(filename):
            print("FILE INSIDE " + folder_name + ":" + filename)
            file_path = folder_name + '\\' + filename
            shutil.copy(file_path, new_file_path)
            i += 1

if i > 1:
    print(f"Files were successfully copied into {new_folder}.")
else:
    if del_folder == 0:
        print("There were no files to copy\n")
        print(new_folder + " has been deleted.")
        path = os.path.abspath(new_folder)
        os.rmdir(path)
    else:
        print("There were no files to copy.")