# *args and **kwargs (very important).
# *args -> variable numbers of positional arguments (becomes a tuple):

def total(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

print(total(10, 20))
print(total(5, 15, 25, 35))


# **kwargs -> variable number of keyword arguments (become a dictionary):

def student_info(**details):
    for key, value in details.items():
        print(f"{key} : {value}")

student_info(name="Rahul", age=21, course="Python")
student_info(name="Sneha", city="Delhi", marks=94)


# you can use both together:

def display(*args, **kwargs):
    print("args: ", args)
    print("kwargs", kwargs)

display(1, 2, 3, name="Python", level="Beginner")