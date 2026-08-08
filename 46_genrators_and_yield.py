# genrators produce value one by one (lazy evaluation) they save memory.

def my_genrator():
    yield 1
    yield 2
    yield 3

gen = my_genrator()
print(next(gen))
print(next(gen))
print(next(gen))


# genrator expression (smile to list comprehension)

gen = (i**2 for i in range(1, 6))
print(next(gen))
print(next(gen))

# example - infinite sequare (carful):

def infinite_counter():
    num = 1
    while True:
        yield num
        num += 1

counter = infinite_counter()
print(next(counter))
print(next(counter))
