num=int(input("Enter number to be checked: "))
is_armstrong = False
temp = num
sum = 0
n=len(str(num))
while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10
if sum == num:
    is_armstrong = True
if is_armstrong==True:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

