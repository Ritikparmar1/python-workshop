#1.wap to find max among 3 numbers using multiple if

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print(a, "is maximum")

if b > a and b > c:
    print(b, "is maximum")

if c > a and c > b:
    print(c, "is maximum")
