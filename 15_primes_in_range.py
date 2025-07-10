lowlim=int(input("Give lower limit of the range : "))
if lowlim<=1:
    print("Lower limit should be greater than 1")
    exit()
uplim=int(input("Give upper limit of the range : "))
if uplim<lowlim:
    print("upper limit should be greater than lower limit")
else:
    for i in range(lowlim,uplim):
        isprime=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                isprime=False
                break
            else:
                continue
        if isprime==False:
            continue
        else:
            print(i)