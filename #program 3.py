#program 3

sub1 = float(input("Enter marks of Subject 1:  "))
sub2 = float(input("Enter marks of Subject 2:  "))
sub3 = float(input("Enter marks of Subject 3:    "))
sub4 = float(input("Enter marks of Subject 4: "))
sub5 = float(input("Enter marks of Subject 5: "))
if (0 <= sub1 <= 100 and
    0 <= sub2 <= 100 and
    0 <= sub3 <= 100 and
    0 <= sub4 <= 100 and
    0 <= sub5 <= 100):
    
    total = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = (total/500) * 100
    print("Total Marks is =",total)
    print("Percentage is =", percentage, "%")
else:
    print("Invalid Input")