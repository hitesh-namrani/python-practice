num1=int(input("Give numerator : "))
num2=int(input("Give denominator : "))
try:
    print(num1/num2)
except ZeroDivisionError:
    print("Denominator cannot be zero")