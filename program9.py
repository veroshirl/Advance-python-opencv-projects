# File Reading and Writing

# Create a text file and write student information
with open("student.txt", "w") as file:
    file.write("Student Name: Veronica\n")
    file.write("Register Number: BTIT101\n")
    file.write("Course: B.Tech Information Technology\n")
    file.write("Marks: 85\n")

# Read the contents of the file
with open("student.txt", "r") as file:
    content = file.read()

# Display the contents
print("Student Information:")
print("-------------------------")
print(content)