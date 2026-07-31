#program 12


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num2 != 0:
        if num1 % num2 == 0:
            print("Yes ! first number is a multiple of the second number")
        else:
              print("No ! first number is niot multiple of the second number")    
else:
    print("0 can't be the multiple of any number")