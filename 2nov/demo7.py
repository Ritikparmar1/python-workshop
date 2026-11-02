#program for dynamic list
a=[]#empty list
n=int(input("enter the limit "))
for i in range(0,n):
    data=int(input("enter new data "))
    a.append(data)
    print("list all data")
    print(a)