# List Comprehensions.
# A short and elegant way to create lists.

# normal way:
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)

# list comprehenion:
squares = [i ** 2 for i in range(1, 6)]
print(squares)

# with condition:
even = [i for i in range(1, 22) if i % 2 == 0]
print(squares)

