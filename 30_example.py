# quick example - (Create, Write, Read)

# Create and write
with open("student.txt", "w") as f:
    f.write("Name : Rahul\n")
    f.write("Age : 22\n")
    f.write("course : Python\n")

# Read the same file
with open("student.txt", "r") as f:
    print(f.read())