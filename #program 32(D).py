#program 32(D)
for i in range(1, 11):
    for space in range(10 - i):
        print(" ", end="")
    for star in range(i):
        print("*", end="")
    print()