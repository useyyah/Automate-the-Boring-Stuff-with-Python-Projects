import os, re, shutil

os.chdir(r"C:\Users\Ozgur2\Desktop\Python_Course\Automate_the_Boring_Stuff _with _Python\Projects\Automate-the-Boring-Stuff-with-Python-Projects\Chapter 10\spams")
path = os.getcwd()

prefix_regex = re.compile(r"(spam)(\d{,3})")

i = 1
for file in os.listdir():
    mo = prefix_regex.search(file)
    if mo:
        old_name = os.path.abspath(file)
        new_suffix = mo.group(1) + str(i).zfill(3) + '.txt'
        new_name = os.path.join(path, new_suffix)
        i += 1
        print(f"Renaming {old_name} to {new_name}...")
        shutil.move(old_name, new_name)