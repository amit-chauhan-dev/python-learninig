# Attributes & Methods:
# Attributes -> variable that belong to the object
# Ṃethod -> function that belong to the class

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age =  age

    def introduse(self):
        print(f"my name is {self.name} and i am {self.age} years old.")

    def is_adult(self):
        return self.age >= 18

s1 = Student("Amit", 20)
s1.introduse()
print(s1.is_adult())