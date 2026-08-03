#program 27

hours = float(input("Enter # of hours worked (-1 to end):      "))
while hours!= -1:
    rate = float(input("Enter hourly rate of the worker ($00.00):    "))

    if hours <= 40:
        salary = hours*rate
    else :
        salary = (40*rate) + (hours-40)*rate*1.5

    print("Salary is    ", salary)
    hours = float(input("Enter # of hours worked (-1 to end): "))
