# Best practice - (with) statment (very impostent)
# using with automatically closes the file even if an arror occurs.

# always prefer this method

# Reading with  'with'
with open("mydata.txt", "r") as file:
    content = file.read()
    print(content)
# file is automatically closed here

# # writing with  'with'
with open("output.txt", "w") as file:
    file.write("This is safe file writing.\n" )
    file.write("No need to call close().\n" )

