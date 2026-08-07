# __init__ method(constructor)

# the __init__method runs automatically when you create an object it is usedto initialize attributes.

class student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age 
        self.course = course

s1 = student("Rahul", 21, "Python")
s2 = student("Priya", 22, "Data since")

print((s1.name), (s1.age), (s1.course))
print((s2.name), (s2.age), (s2.course))

# self refers to the current object
