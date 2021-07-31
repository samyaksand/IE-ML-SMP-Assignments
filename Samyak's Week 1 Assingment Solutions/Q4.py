list = []

a = int(input("Enter the Total Number of List Elements: "))
for i in range(1, a + 1):
    value = int(input("Enter the Value of %d Element : " %i))
    list.append(value)

list.sort()
print("Ascending Order is : ", list)

asc = sorted(list)
desc = sorted(list,reverse = True)
print("Descending Order is : ", desc)