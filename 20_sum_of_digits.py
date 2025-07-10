num=int(input("Give number : "))
if num>=0:
    temp=num
else:
    temp=-num
while temp>=10:
    digisum=0
    while temp>0:
        digisum+=temp%10
        temp//=10
    temp=digisum
print("single digit sum of",num,"is",temp)