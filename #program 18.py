#program 18
days = int(input("Enter late days: "))
if days <= 5:
    fine = days * 0.50
    print("Fine =", fine, "rupees")
elif days <= 10:
    fine = days * 1
    print("Fine =", fine, "rupees")
elif days <= 30:
    fine = days * 5
    print("Fine =", fine, "rupees")
else:
    print("Membership Cancelled")
