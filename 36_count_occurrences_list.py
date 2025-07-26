ls=list()
size=int(input("Give number of elements in list : "))
for i in range(size):
    ls.append(input(f"Give element {i+1} of list : "))
count=ls.count(input("Give which element is to be counted : "))
print(count)