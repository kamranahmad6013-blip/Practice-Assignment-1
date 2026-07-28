# Program 9

gender = input("Driver is Male or Female (M/F): ")
status = input("Driver is Married or Unmarried (Mar/Unmar): ")
age = int(input("Enter your age: "))

if status == "mar":
    print("The driver is insured")

elif status == "unmar" and gender == "m" and age > 30:
    print("The driver is insured")

elif status == "unmar" and gender == "f" and age > 25:
    print("The driver is insured")

else:
    print("The driver is not insured")