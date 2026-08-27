# Regular Expression for Email Validation

import re

email = input("Enter your email address: ")

# Regular expression pattern for email validation
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Check whether the email is valid
if re.match(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")