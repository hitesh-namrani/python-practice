from functools import reduce
nums=[]
size=int(input("Give number of elements in list : "))
for i in range (size):
    nums.append(int(input(f"Give number {i+1} in list : ")))
#filter()
f_nums=list(filter(lambda x : x%2==0,nums))
print(f_nums)
#map()
squared_list=list(map(lambda x:x**2,nums))
print(squared_list)
#reduce()
product=reduce(lambda x,y:x*y,nums)
print(product)