# # Useful Built-in Modules.

# # A. math module
import math 

print(math.sqrt(64))
print(math.pow(2, 5))       # 2^5 = 32
print(math.floor(4.9))      # 4
print(math.ceil(4.1))       # 5
print(math.factorial(6))    # 720
print(math.sin(math.pi/2))  # 1.0


# B. random module
import random

print(random.random())          # random float between 0 and 1
print(random.randint(1, 10))    # random integer 1 to 10
print(random.choice(["apple", "banana", "mango"]))

numbers = [10, 20, 30, 40, 50]
print(random.sample(numbers, 3))    # pick 3 unique numbers
random.shuffle(numbers)
print(numbers)                      # list is shuffled


# C. datetime module
from datetime import datetime, date, timedelta

now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.strftime("%d-%m-%y %H:%M%S"))

today = date.today()
print(today)

tomorrow = today + timedelta(days=1)
print(tomorrow)