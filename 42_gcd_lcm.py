def hcf(a,b):
    hcf=1
    if a>b:
        for i in range (1,b+1):
            if a%i==0:
                if b%i==0:
                    hcf=i
                else:
                    continue
            else:
                continue
    else:
        for i in range (1,a+1):
            if a%i==0:
                if b%i==0:
                    hcf=i
                else:
                    continue
            else:
                continue
    print(f"HCF is {hcf}")
def lcm(a,b):
    i=1
    while i%a!=0 or i%b!=0:
        i+=1
    print(f"LCM is {i}")
num1=int(input("Give number 1 : "))
num2=int(input("Give number 2 : "))
lcm(num1,num2)
hcf(num1,num2)