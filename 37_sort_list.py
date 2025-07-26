ls=list()
size=int(input("Give number of elements in list : "))
for i in range(size):
    ls.append(int(input(f"Give element {i+1} of list : ")))
ls.sort()
print(ls)