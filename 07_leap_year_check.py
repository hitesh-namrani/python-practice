# Get year from the user
year=int(input("Give year to be checked : "))
# Check if year is divisible by 400 
if year%400==0:
    # If yes the year is a leap year 
    print(year,"is a leap year")
# If not divisible by 400 then check divisibility by 100  
elif year%100==0:
    # If divisible by 100 then year is not a leap year
    print(year,"is not a leap year")
# If not divisible by both 400 and 100 then check divisibility by 4
elif year%4==0:
    # If divisible by 4 the year is a leap year
    print(year,"is a leap year")
# If not divisible by 400,100 and 4 then the year is not a leap year
else:
    print(year,"is not a leap year")