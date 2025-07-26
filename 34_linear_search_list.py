size=int(input("Give number of elements in list : "))
ls=list()
for i in range(size):
    ls.append(int(input(f"Give number {i+1} in list : ")))
num=int(input("Give number to be found in the list : "))
for i in range(0,size):
    if num==ls[i]:
        print("number is present in the list at index",i)