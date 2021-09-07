import os
import re
import pprint

files = []
for file in os.listdir('.'):
    if file.endswith('.txt'):
        files.append(file)

user_regex = input("Which expression you are looking for?\n")
search_regex = re.compile(user_regex, re.I)

regex_file = []
for filename in files:
    open_file = open(filename)
    read_file = open_file.read()
    if search_regex.search(read_file):
        regex_file.append(filename)

pprint.pprint(regex_file)