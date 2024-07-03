'''Write a Python program that matches a string that has an 'a' followed by two to three 'b'.'''
import re


input_str = input("Enter a string: ")

# Regular expression pattern
pattern = r'a(b{2,3})'

# Check if pattern matches
if re.search(pattern, input_str):
    print("Pattern matched!")
else:
    print("Pattern not matched.")

