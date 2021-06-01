# When running, this will find and print all phone 
# numbers and emails found from the clipboard. 
# To use it, select all text on a given page 
# and copy it. Then run this program.

import pyperclip
import re


phoneRegex = re.compile(r'''(

    (\d{3}|\(\d{3}\))?  # optional area code
    (\s|-|\.)?  # separator
    (\d{3})  # first 3 digits
    (\s|-|\.)?  # separator
    (\d{4})  # last 4 digits
    (\s(ext|x|ext.)\s*\d{1,5})?  # extension
    )''', re.VERBOSE)


emailRegex = re.compile(r'''(

    [a-zA-z0-9._%+-]+  # username
    @                  # @ symbol
    [a-zA-Z0-9.-]+     # domain name
    (\.[a-zA-Z]{2,4})  # dot-something
    )''', re.VERBOSE)


text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[7] != '':
        phoneNum += ' x' + groups[7]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])


if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
