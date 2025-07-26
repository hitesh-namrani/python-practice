num=int(input("Give number to be checked : "))
if num<0:
    print(num,"is not a palindrome")
else:
    temp=num
    rev=0
    for i in range(1,len(str(temp))+1):
        rev=(rev*10)+(temp%10)
        temp//=10
    if num==rev:
        print(num,"is a palindrome")
    else:
        print(num,"is not a palindrome")