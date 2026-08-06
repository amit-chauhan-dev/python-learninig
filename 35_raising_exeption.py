# Raising exception (raise)
# you can manually raise an exception when somthing is wrong.

age = int(input("Enter your age: "))

if age < 0:
    raise ValueError("Age cannot be negative")
elif age > 120:
    raise ValueError("Age iss not high")
else:
    print("valid age", age)