# Polymorphism:
# same method name behaves defferently in different classes.

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("meow")

class Cow:
    def sound(self):
        print("moo")

def make_sound(animal):
    animal.sound()

make_sound(Dog())
make_sound(Cat())
make_sound(Cow())