'''Split a string at uppercase letters.'''

import re

lol = input("one string with uppercases in there:")
res = re.split('(?=[A-Z])', lol)
print(res)
