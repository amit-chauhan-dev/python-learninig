# for loop (best for known numbers of repetition)

# 1. simple for loop 
for i in range(5):  # 0 to 4
    print(i)

# 2. loop over list 
fruits = ["apple", "banana", "mango"]
for fruits in fruits:
    print(f"I like {fruits} ")

# while loop (best when you don't knoe how many times)
count = 0
while count < 5:
    print(count)
    count += 1  # very important otherwise infinite loop 