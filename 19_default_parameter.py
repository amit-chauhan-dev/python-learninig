# defaut parameters .

def greet(name="guest"):
    print(f"Hello, {name}!")

greet("Rahul")  # Hello, Rahul!
greet()         # Hello, guest!

#  you can also mix normal + default parameters:

def introduce(name, age= 18, city="delhi"):
    print(f"name:{name}, age:{age}, city:{city}")

introduce("Priya")
introduce("Amit", 21)
introduce("Sneha", 22, "mumbai")