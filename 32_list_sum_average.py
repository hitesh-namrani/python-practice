list1=input("Give all elements of list : ").split()
list1=[int(i) for i in list1]
sum=0
avg=0
for i in list1:
    sum+=i
avg=sum/len(list1)
if avg%1==0:
    print(f"the sum of all members of list is {sum} and avg of all members of list is {int(avg)}")
else:
    print(f"the sum of all members of list is {sum} and avg of all members of list is {avg}")