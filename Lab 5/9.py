'''Insert spaces between words starting with capital letters'''

import re

lol = input("Make a camelCaseString:")
spaced = re.sub('([a-z])([A-Z])', r'\1 \2', lol)

print(f"The answer: {spaced}")