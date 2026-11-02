
n = int(input("Enter the value of n: "))
s = 0
fact = 1

for i in range(1, n + 1):
    fact = fact * i
    s = s + 1 / fact

print("Sum of series =", s)
