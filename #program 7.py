#program 7

Number = int(input("Enter a five-digit number: "))
a = Number%10
b = (Number//10)%10
c = (Number//100)%10
d = (Number//1000)%10
e = Number//10000

sum = a + b + c + d + e
print(sum)