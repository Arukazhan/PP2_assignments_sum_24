'''Convert snake case string to camel case string.'''

import re

snake_case = input("We need a snake_case string:")

camelC = re.sub('_([a-zA-Z])', lambda match: match.group(1).upper(), snake_case)
camelC = camelC[0].lower() + camelC[1:]

print("CamelCase string:", camelC)
