file = open("mydata.txt", "r")
content = file.read()
print(content)
file.close()    # always close the file


# read line by line 
file = open("mydata.txt", "r")
print(file.readline())  # read first line
print(file.readline())  # read secoond line
file.close()


# read all lines as a list
file = open("mydata.txt", "r")
lines = file.readlines()
print(lines)
file.close()