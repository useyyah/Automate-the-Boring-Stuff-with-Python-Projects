import os, re, shutil

os.chdir(r"C:\Users\Ozgur2\Desktop\Python_Course\Automate_the_Boring_Stuff _with _Python\Projects\Automate-the-Boring-Stuff-with-Python-Projects\Chapter 10\spams")
path = os.getcwd()
regex = re.compile('(spam)(\d{,3})')

replace = input("Where would you like to insert a gap at?\n")
replace = str(replace.zfill(3))

i = 1
for file in os.listdir():
    mo = regex.search(file)
    if mo:
        old_name = os.path.abspath(file)
        if mo.group(2) == replace:
            i += 1
        new_suffix = "spam_" + str(i).zfill(3) + '.txt'
        new_name = os.path.join(path, new_suffix)
        i += 1
        shutil.move(old_name, new_name)

rename_regex = re.compile('(spam_)(\d{3})')
i = 1
for file in os.listdir():
    mo = rename_regex.search(file)
    if mo:
        old_name = os.path.join(path, mo.group(1) + mo.group(2) + '.txt')
        new_name = os.path.join(path, re.sub(mo.group(1), 'spam', file))
        print(f"Renaming {old_name} to {new_name}...")
        shutil.move(old_name, new_name)