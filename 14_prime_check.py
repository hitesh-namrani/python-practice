num=int(input("Give number to be checked : "))
if num<2:
    print(num,"is not a prime number")
else:
    isprime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            isprime=False
            break
        else:
            continue
    if isprime==False:
        print(num,"is not a prime number")
    else:
        print(num,"is a prime number")