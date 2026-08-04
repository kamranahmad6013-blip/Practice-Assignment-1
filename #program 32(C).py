#program 32(C)
 
for i in range(10, 0, -1):
    for space in range(10 - i):
        print(" ", end="")
    for star in range(i):
        print("*", end="")
    print()