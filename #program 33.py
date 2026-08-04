#program 33
x = 4
y = 6
a = 5
b = 5
g = 4
i = 3
j = 7






# A
print("a)")
print("Original   =", not (x < 5 and y >= 7))
print("Equivalent =", (not (x < 5)) or (not (y >= 7)))

print()

# B
print("b)")
print("Original   =", not (a == b or g != 5))
print("Equivalent =", (not (a == b)) and (not (g != 5)))

print()

# C
print("c)")
print("Original   =", not ((x <= 8) and (y > 4)))
print("Equivalent =", (not (x <= 8)) or (not (y > 4)))

print()

# D
print("d)")
print("Original   =", not ((i > 4) or (j <= 6)))
print("Equivalent =", (not (i > 4)) and (not (j <= 6)))