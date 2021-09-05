import re

def strong_password(password):
    regex_count = 0
    for regex in regex_list:
        if regex.search(password) is None:
            print("Sorry, your password is not strong enough.")
            break
        else:
            regex_count += 1
            continue
    if regex_count == 4:
        print("Congrats. Your password is strong enough!")

length_regex = re.compile('.{8,}')
lower_case_regex = re.compile('[a-z]+')
upper_case_regex = re.compile('[A-Z]+')
digit_regex = re.compile('[\d]+')

regex_list = [length_regex,
              lower_case_regex,
              upper_case_regex,
              digit_regex]

user_password = input("Please type in a password:\n")
strong_password(user_password)

