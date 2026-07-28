# Sets (Unique Elements Only)

numbers = {1, 2, 3, 3, 4, 2}
print(numbers)  # duplicates removed

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# Use when: you need unique values only
