# Program 9

gender = input("Driver is Male or Female (M/F): ")
status = input("Driver is Married or Unmarried (Mar/Unmar): ")
age = int(input("Enter your age: "))

if status == "Mar":
    print("The driver is insured")

elif status == "Unmar" and gender == "M" and age > 30:
    print("The driver is insured")

elif status == "Unmar" and gender == "F" and age > 25:
    print("The driver is insured")

else:
    print("The driver is not insured")