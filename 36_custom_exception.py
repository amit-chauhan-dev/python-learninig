# Creating custom exception.
# you can make your own exception classes

class NegativeNumberError(Exception):
    pass

def check_positive(num):
    if num < 0:
        raise NegativeNumberError("Number cannot be negative!")
    return num

try:
    number = int(input("Enter a positive number: "))
    print("You entered:", check_positive(number))
except NegativeNumberError as e:
    print("Error:", e)
except ValueError:
    print("Please enter a valid integer")