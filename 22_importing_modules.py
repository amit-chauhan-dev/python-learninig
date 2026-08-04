#  there are diffrent ways to  import.

# Method 1: full import
import math

print(math.sqrt(16))
print(math.pi)
print(math.ceil(4.2))
print(type(math))


# Method 2: import specific things
from math import sqrt, pi, ceil   # they are functions , methods (sqrt , pi , ceil)

print(sqrt(25))
print(pi)
print(ceil(3.1))


# Method 3: import with alias (nickname)
import math as m

print(m.sqrt(49))
print(pi)


# Method 4: import everything (Not recommended)
from math import *

print(sqrt(49))
print(pi)

# (Avoid this in bigger projects because it can cause name conflicts.)
