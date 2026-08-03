#program 20
A = float(input("Enter marks in A: "))
B = float(input("Enter marks in B: "))
if A >= 55 and B >= 45:
    print("Pass")
elif A >= 45 and A < 55 and B >= 55:
    print("Pass")
elif A >= 65 and B < 45:
    print("reappear in B")
else:
    print("Fail")