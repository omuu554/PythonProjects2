#תרגיל 4

Name = input("Please enter a name: ") #מקבל שם
CurrYear = int(input("Please enter current year: "))#מקבל ש
Age = int(input("Please enter the age of 'Name': "))
FutuYear = int(input("Please enter the future year: "))

print(f"{Name} will be {Age+(FutuYear-CurrYear)} in the year {FutuYear}")
