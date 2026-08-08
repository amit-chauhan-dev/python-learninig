# Iterators:
# An iterator is an object that can be iterated (loopd) using __iter__() and __next__()

nums = [10, 20, 30, 40]
it = iter(nums)

print(next(it))
print(next(it))
print(next(it))
# print(next(it)) → StopIteration error

# creating custom iterator:
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        Value = self.current
        self.current -= 1
        return Value
    
for num in CountDown(5):
    print(num)