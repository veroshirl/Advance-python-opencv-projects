# Regular Expression for Indian Mobile Number Validation

import re

mobile = input("Enter your mobile number: ")

# Indian mobile number: exactly 10 digits and starts with 6, 7, 8, or 9
pattern = r'^[6-9][0-9]{9}$'

# Validate the mobile number
if re.match(pattern, mobile):
    print("Valid Indian mobile number")
else:
    print("Invalid Indian mobile number")