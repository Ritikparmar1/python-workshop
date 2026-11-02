#program for fabonacci series
n=int(input("enter the limit "))
a=0
b=1
print("fabonacci series is ")
print(a,b,end=" ")

for i in range(1,1+n):
    c=a+b
    print(c,end=" ")
    a=b
    b=c