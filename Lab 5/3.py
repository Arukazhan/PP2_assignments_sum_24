'''Write a Python program to find sequences of lowercase letters joined with a underscore.'''
import re

txt = input()
match = re.findall("[a-z]+_", txt)
print(match)
