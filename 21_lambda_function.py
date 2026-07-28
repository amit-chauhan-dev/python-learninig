# Lambda functions(anonymous(one-line function))

# normal function
def square(x):
    return x * x

# Lambda version
square = lambda x: x * x
print(square(5))

# common uses
add = lambda a, b: a + b
print(add(10, 20))

# with map, filter(we'll use more later)

numbers = [1, 2, 3, 4, 5]
square = list(map(lambda x: x ** 2, numbers))
print(square)   # [1, 4, 9, 16, 25]