num1=int(input("enter first number : "))
operator=int(input("enter\n1 for '+',\n2 for '-',\n3 for'*',\n4 for / : "))
num2=int(input("enter second number : "))
if operator==1:
    print(num1,"+",num2,"=",num1+num2)
elif operator==2:
    print(num1,"-",num2,"=",num1-num2)
elif operator==3:
    print(num1,"*",num2,"=",num1*num2)
elif operator==4:
    print(num1,"/",num2,"=",num1/num2)
else:
    print("invalid operator")