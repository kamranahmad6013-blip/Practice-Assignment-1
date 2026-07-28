#program 9
gender = input("Driver is Male or Female (M/F)").lower()
status = input("Driver is married or unmaried (Mar/Unmar)").lower()
age = int(input("Enter your age "))
if status =="mar" :
      print("\n   The driver is insured")
elif status=="unmar" and gender=="m" and age >= 30:
    print("\n   The driver is insured ")
elif status == "unmar"  and gender == "f" and age >= 25:  
    print("\n   The driver is insured")
else :#Conditions Are not met .
  print("The driver is not insured")
