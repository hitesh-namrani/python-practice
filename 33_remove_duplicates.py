list1=input("Give all members of list : ").split()
for i in range(0,len(list1)):
    for j in range(len(list1)-1,i,-1):
        if list1[i]==list1[j]:
            list1.pop(j)
        else:
            continue
    
print("after removing all duplicates list is",list1)