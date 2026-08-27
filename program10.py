# File Analysis Program

# Read the text file
with open("student.txt", "r") as file:
    content = file.read()

# Count lines, words, and characters
lines = content.splitlines()
words = content.split()
characters = len(content)

# Display the results
print("File Analysis")
print("-------------------------")
print("Number of lines:", len(lines))
print("Number of words:", len(words))
print("Number of characters:", characters)