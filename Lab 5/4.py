'''Write a Python program to find the sequences of one upper case letter followed by lower case letters.'''

import re

lol = input()
a = re.findall('[A-Z]{1}[a-z]+', lol)
print(a)