# JSON Data Parsing and Conversion

import json

# Create a Python dictionary containing student details
student = {
    "name": "Veronica",
    "register_number": "BTIT101",
    "course": "B.Tech Information Technology",
    "marks": 85
}

# Convert Python dictionary into JSON string
json_string = json.dumps(student)

print("Python Dictionary:")
print(student)

print("\nJSON String:")
print(json_string)

# Convert JSON string back into Python dictionary
python_dictionary = json.loads(json_string)

print("\nPython Dictionary after JSON conversion:")
print(python_dictionary)