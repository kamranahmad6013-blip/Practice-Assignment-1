#program 25

n = int(input("How many numbers do you want to enter  ?        "))

num = int(input("Enter number:                                 "))
largest = num 
smallest = num
for i in range(1,n):
    num = int(input("Enter number: "))
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
difference = largest - smallest

print("Largest Number =", largest)
print("Smallest Number =", smallest)
print("Range =", difference)                                    