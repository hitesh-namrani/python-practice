num=int(input("Enter number to be reversed : "))
temp=num
rev_num=0
for i in range(1,len(str(num))+1) :
    rev_num=(rev_num*10)+(temp%10)
    temp//=10
print("The reverse of",num,"is",rev_num)     