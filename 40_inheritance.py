# inheritance:
# inheritance allows a class to use properties an method of another class.

# A. Single inheritance.
class person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)

class student(person):  # student inherits from person
    def __init__(self, name, course):
        super().__init__(name)  # call person cunstructor
        self.course = course

    def show_course(self):
        print("course:", self.course)

s1 = student("Rahul", "Python")
s1.show_name()
s1.show_course()


# B. multilevel inheritance.
class A:
    def method_a(self):
        print("This is class A ")

class B(A):
    def method_b(self):
        print("This is class B ")

class C(B):
    def method_c(self):
        print("This is class C ")

obj = C()
obj.method_a()
obj.method_b()
obj.method_c()


# C. Multiple inheritance
class Father:
    def skill(self):
        print("Father: gardening")

class Mother:
    def skill(self):
        print("Mother: cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skill()   # uses father method (method Resolution order)
