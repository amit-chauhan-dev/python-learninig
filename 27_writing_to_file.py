# Warning: mode 'w' will delete previous  content if the file already exists.

file = open("note.txt", "w")
file.write("Hello, this is my first file, \n")
file.write("i'm learning python file handling. \n")
file.close()


# writing multiple lines:
lines = ["line 1\n", "line 2\n", "line 3\n"]
file = open("note1.txt", "w")
file.writelines(lines)
file.close()
