print("""
# Pattern A

for i in range(1, 11):
    for j in range(i):
        print("*", end="")
    print()
""")

for i in range(1, 11):
    for j in range(i):
        print("*", end="")
    print()

print()

print("""
# Pattern B

for i in range(10, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
""")

for i in range(10, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

print()

print("""
# Pattern C

for i in range(10, 0, -1):
    for space in range(10 - i):
        print(" ", end="")
    for star in range(i):
        print("*", end="")
    print()
""")

for i in range(10, 0, -1):
    for space in range(10 - i):
        print(" ", end="")
    for star in range(i):
        print("*", end="")
    print()

print()

print("""
# Pattern D

for i in range(1, 11):
    for space in range(10 - i):
        print(" ", end="")
    for star in range(i):
        print("*", end="")
    print()
""")

for i in range(1, 11):
    for space in range(10 - i):
        print(" ", end="")
    for star in range(i):
        print("*", end="")
    print()