# loop controls : break, continuse, pass
for i in range(10):
    if i == 3:
        continue    # skip this iteration
    if i == 7:
        break   # stop the whole loop
    print(i)

# pass -> does nothing (used as placeholder)
for i in range(5):
    pass 
