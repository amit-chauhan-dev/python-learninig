# try and except (basic handling)

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("result: ", result)
except:
    print("Somthing went wrong: ")

# Better way - catch specific error 

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result: ", result)
except ZeroDivisionError:
    print("Please enter a valid number! ")