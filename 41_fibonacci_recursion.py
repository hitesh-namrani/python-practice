def fib(num,count=0,a=0,b=1):
    if count>=num:
        return
    print(a)
    a,b=b,b+a
    count+=1
    return fib(num,count,a,b)
num=int(input("Give number of terms required : "))
fib(num=num)