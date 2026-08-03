#program 23



p = 0 # Positive Number
n = 0 # Negative Number
z = 0 # Zero

choice = "y"


while choice == "y":


    number = int(input("Enter Any Number      "))

    if number > 0:
        p = p  + 1
    elif number < 0:
        n = n + 1
    else:
        z = z + 1
    choice = str(input("Do you want enter any other number (y/n)"))
#        y For Yes ! or n For No !




print("Positive Numbers   " ,p)
print("Negative Numbers   " ,n)
print("Zero Numbers       " , z)
