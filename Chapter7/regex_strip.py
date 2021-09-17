import re

test_string = input("Please enter a string to strip: ")
removal = input("What characters do you want to remove? (Press enter for whitespace)")

def white_strip(string, remove):
    if remove != '':
        strip_regex = re.compile(remove)
        new_string = strip_regex.sub('', string)
        return new_string
    else:
        strip_regex = re.compile('^\s*')
        new_string = strip_regex.sub('', string)
        strip_regex = re.compile('\s$')
        new_string = strip_regex.sub('', new_string)
        return new_string

new_string = white_strip(test_string, removal)
print(new_string)