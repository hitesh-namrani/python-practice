list1=input("Give all elements of list : ").split()
list1=[int(i) for i in list1]
max=list1[0]
min=list1[0]
for i in list1:
    if(i>max):
        max=i
    else:
        continue
for i in list1:
    if (i<min):
        min=i
    else:
        continue
print(f"max in list is {max} and min is {min}")