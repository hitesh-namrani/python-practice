num=int(input("Give number whose digits are to be counted : "))
digits=len(str(num))
if num>=0:
    print(num,"has",digits,"digits")
else:
    print(num,"has",digits-1,"digits")