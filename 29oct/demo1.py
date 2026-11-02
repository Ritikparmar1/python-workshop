#1.wap to find max among 3 numbers using ladder if

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print(a, "is maximum")

elif b > c:
    print(b, "is maximum")

else:
    print(c, "is maximum")
