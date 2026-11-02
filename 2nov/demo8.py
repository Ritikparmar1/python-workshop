#list with membership operator
list1=[2,56,7,9,10]
s=int(input("enter data to be search"))
result=s in list1
if(result):
    print("data is found")
else:
    print("data is not found")
    