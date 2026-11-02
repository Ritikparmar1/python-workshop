n=int(input("enter any no."))
res=0
temp=n
while(n!=0):
    a=n%10
    res=(a**3)+res
    n=n//10

if(res==temp):
    print("no. is armstrong")
else:
    print("no. is not armstrong")