'''Convert a given camel case string to snake case'''

import re

camelCase = input("Make a camelCaseString:")
snake_case_string = re.sub('(?<!^)(?=[A-Z])', '_', camelCase).lower()

'''
1. re.sub - function
2. r'(?<!^)(?=[A-Z]) - a syntax called regular expression
r - raw string (\t, \d )
(?<!...) - Negative Lookbehind Assertion
3. (?<!^) - not at the beginning
4. (?=[A-Z]) - 

'''
print(f"Snake case: {snake_case_string}")

