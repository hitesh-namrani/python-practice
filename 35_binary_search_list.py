ls=list()
size=int(input("Give number of elements in list : "))
for i in range (size):
    ls.append(int(input(f"Give element {i+1} in list : ")))
ls.sort()
print(f"sorted list is {ls}")
num=int(input("Give number to be found in list : "))
low=0
high=size-1
mid=(low+high)//2
while(low<=high):
    if ls[mid]==num:
        print(f"{num} is present at index {mid}")
        break
    elif num>ls[mid]:
        low=mid+1
        mid=(low+high)//2
    else:
        high=mid-1
        mid=(low+high)//2
else:
    print("number not found in list")