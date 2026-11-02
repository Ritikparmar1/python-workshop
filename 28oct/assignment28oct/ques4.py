
basic = float(input("Enter basic salary: "))
bonus = float(input("Enter bonus: "))
hra = float(input("Enter HRA: "))

pf = basic * 7.8 / 100

total_salary = basic + bonus + hra
net_salary = total_salary - pf

print("PF =", pf)
print("Total Salary =", total_salary)
print("Net Salary =", net_salary)
