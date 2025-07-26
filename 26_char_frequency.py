string1=input("Give string : ")
string=string1.upper()
for i in range(65,91):
    num=0
    for j in range(len(string)):
        if string[j]==chr(i):
            num+=1
    if num>0:
        print(f"{chr(i)}={num}")