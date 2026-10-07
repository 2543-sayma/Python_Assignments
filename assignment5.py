import re

text = input("Enter string")
if re.match("^[a-zA-Z0-9]+$",text):
    print("Valid string")
else:
    print("Invalid string")