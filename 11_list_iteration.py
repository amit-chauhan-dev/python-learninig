# list iteration (most common in real code)
numbers = [10, 20, 30, 40, 50]

# method 1: Direct
for num in numbers:
    print(num)

# method 2: with Index
for i, num in enumerate (numbers):
    print(f" Index {i} : {num} ")

# method 3: while loop
i = 10
while i < len (numbers):
    print(numbers[i])
    i += 1
    