#program 29

num = 1

for i in range(1, 5):
    print(" " * (5 - i), end="")

    for j in range(i):
        print(num, end=" ")
        num = num + 1
    print(" ")