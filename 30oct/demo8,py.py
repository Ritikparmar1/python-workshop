
n = int(input("Enter the number of terms: "))
ct=0
b=0
for i in range(1, n + 1):
    if(i%2==0):
     print("even no is ",i)
     ct+=1
    else:
     print("odd no is",i)
     b+=1
print("total even no is ",ct)
print("total odd no is ",b)