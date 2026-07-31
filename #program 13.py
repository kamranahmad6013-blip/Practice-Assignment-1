#program 13
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(num1,"  is larger than ",num2)
elif num2 > num1 :
    print(num2,"  is larger than ",num1)    
else:
    print("Both numbers are equal")