n=int(input("enter any no."))
res=0
temp=n
while(n!=0):
    a=n%10
    res=(res*10)+a
    n=n//10

if(res==temp):
    print("no. is palindrome")
else:
    print("no. is not palindrome")