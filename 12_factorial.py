n=int(input("Give number whose factorial is required : "))
fact=1
if n<0:
    print("Negative integers are not allowed")
else:
    for i in range(2,n+1):
        fact*=i
    print("factorial of",n,"is",fact)