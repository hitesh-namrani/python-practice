def sum(a,b):
    print(f"{a}+{b}={a+b}")
    return
def mul(a,b):
    print(f"{a}*{b}={a*b}")
    return
def divide(a,b):
    print(f"{a}/{b}={a/b}")
    return
def minus(a,b):
    print(f"{a}-{b}={a-b}")
num1=int(input("Give number 1 : "))
operator=input("Give operator : ")
num2=int(input("Give number 2 : "))
if operator=='+':
    sum(num1,num2)
elif operator=='-':
    minus(num1,num2)
elif operator=='*':
    mul(num1,num2)
elif operator=='/':
    divide(num1,num2)
else:
    print("Enter valid operator")