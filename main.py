import mymodule

print(mymodule.greet("Rahul"))
print(mymodule.add(10, 20))
print(mymodule.pi_value)

# or using from
from mymodule import greet, add

print(greet("Priya"))
print(add(5, 7))