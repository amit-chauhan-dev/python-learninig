# multiple exception in one line. 

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except (ZeroDivisionError, ValueError):
    print("Invalid input or division by zero: ")
