#! python3
# backup_to_zip.py - Copies and entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def backup_to_zip(folder):
    # Back up the entire contents of 'folder' into a ZIP file.

    folder = os.path.abspath(folder)    # make sure folder is absolute

    # Figure out the filename this code should based on
    # what files already exist.
    number = 1
    while True:
        zip_file_name = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_file_name):
            break
        number = number + 1

    # Create the ZIP file.
    print(f"Creating {zip_file_name}...")
    backup_zip = zipfile.ZipFile(zip_file_name, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f"Adding files in {foldername}...")
        # Add the current folder to the ZIP file.
        backup_zip.write(foldername)

    # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue # don't back up the backup ZIP files
            backup_zip.write(os.path.join(foldername, filename))
    backup_zip.close()
    print("Done.")

backup_to_zip("C:\\Users\\Ozgur2\\Desktop\\Python_Course\\Automate_the_Boring_Stuff _with _Python\\Projects\\Automate-the-Boring-Stuff-with-Python-Projects\\Chapter 9")
