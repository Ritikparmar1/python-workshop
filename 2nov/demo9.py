
# Linear Search using Membership Operator

list1 = [10, 20, 30, 40, 50]

s = int(input("Enter the element to search: "))
found = 0
n = len(list1)

for i in range(0, n):
    if list1[i] == s:
        found = 1
        break

if found == 1:
    if s in list1:
        print("Element found in the list at position", i + 1)
else:
    print("Element not found in the list")
