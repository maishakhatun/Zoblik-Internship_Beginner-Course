# Exercise: Validate User Input with Regex

import re

username = input("Enter your username: ").strip()

# Regex pattern
pattern = r"[a-zA-Z]+"

# Validate using re.fullmatch()
if re.fullmatch(pattern, username):
    print(f"{username} is a Valid Username!")
else:
    print(f"{username} is an Invalid Username.")