yr=int(input("enter year = "))
if(yr%400==0):
    print("year is a leap year")
elif(yr%4==0):
    print("year is a leap year")
elif(yr%100==0):
    print("year is not a leap year")
else:
    print("year is not a leap year")