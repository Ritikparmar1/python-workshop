#program for different different arithmetic operation
print("press1 for addition: ")
print("press2 for subtraction: ")
print("press 3 for multiply: ")
print("press 4 for divide: ")
a=int(input("enter first no.: "))
b=int(input("enter second no.: "))
ch=int(input("enter your choice: "))
if(ch==1):
    c=a+b
    print(c)
elif(ch==2):
    c=a-b
    print(c)
elif(ch==3):
    c=a*b
    print(c)
elif(ch==4):
    c=b/a
    print(c)
else:
    print("enter valid choice:")
