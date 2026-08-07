# Magic / Dunder Methods:
# special method with double underscors.
# thay give special behavior to objects.

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}"

    def __len__(self):
        return self.pages

    def __add__(self, other):
        return self.pages + other.pages

b1 = Book("Python Basices", 300)
b2 = Book("advanced python", 450)

print(b1)           # Uses __str__
print(len(b1))      # Uses __len__
print(b1 + b2)      # Uses __add__