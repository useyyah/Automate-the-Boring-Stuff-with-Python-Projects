#! python3
# american_european_dates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import os
import re
import shutil

# Create a regex that matches files with the American date format.
date_pattern = re.compile(r"""^(.*?) # all text before the date
     ((0|1)?\d)-                     # one or two digits for the month
     ((0|1|2|3)?\d)-                 # one or two digits for the day
     ((19|20)\d\d)                   # four digits for the year
     (.*?)$                          # all text after the date
     """, re.VERBOSE)

# Loop over the files in the working directory.
for american_file in os.listdir('.'):
    mo = date_pattern.search(american_file)

    # Skip files without a date.
    if mo is None:
        continue

    # Get the different parts of the filename.
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    # Form the European-style filename.
    euro_file = before_part + day_part + '-' + month_part + '-' + year_part + after_part

    # Get the full, absolute file paths.
    abs_working_dir = os.path.abspath('.')
    american_file = os.path.join(abs_working_dir, american_file)
    euro_file = os.path.join(abs_working_dir, euro_file)

    # Rename the files.
    shutil.move(american_file, euro_file)
