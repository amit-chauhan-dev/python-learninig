# finally block 
# the finally block always runs, whether there was an error or not.
# Useful for closing filse or cleaning up resources.

try:
    file = open("Data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("file not found: ")
    # file.close() woude go here if the file was oppend 

# Best practice with (with) + exception handling:

try:
    with open("Data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Sorry, the file does not exist.")
    