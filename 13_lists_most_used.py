# Lists (most used)

fruits = ["apple", "banana", "mango", "orange"]

# Indexing & Slicing 
print(fruits[1])    # banana
print(fruits[1:3])  # ['banana', 'mango']

# Important Method
fruits.append("grape")   # add at end
fruits.insert(1, "kiwi") # add at position
fruits.remove("banana")  # remove by value
popped = fruits.pop()    # remove last value ,, Remove and return item at index (default last).
fruits.sort()            # sort alphabeticaly
fruits.reverse()         # reverse order
print(fruits)

# Lists are mutable (you can change them )