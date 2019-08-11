def checkyear(y):
    if y%4==0:
        return True
    else:
        return False
year=int(input("Enter a YEAR:"))
if checkyear(year):
    print(year,"is a leap year!!!")
else:
    print(year,"is not a leap year!!!!!!")
        
