principal=int(input("Give principal amount : "))
interest_rate=float(input("Give interest rate per annum : "))
time=int(input("Give number of years : "))
interest=principal*interest_rate*time/100
print("simple interest over the given principal, interest rate and time is",interest,"and total investment is",interest+principal)