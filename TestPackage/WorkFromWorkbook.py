a = 10
b = 5

Sum = a + b
print(Sum)
print("The sum is: ", Sum) # This is the sum of the numbers a and b

Name = input("Please enter a name: ")
Age = int(input("Please enter the age of the man: "))
CurrYear = int(input("Please enter the current year: "))
print(f"The man named {Name} will be 100 at the year {CurrYear+ 100 - Age}")

CurrWage = int(input("Please enter the current wage of the man: "))#שכר
FutuPrec = float(input("Please enter the precentage of wage increase: "))#אחוז האלעה
print(f"The current wage of the man after the increase will be {CurrWage + CurrWage * (FutuPrec / 100)} shekels")

Radius = float(input("Please enter the radius of the circle: "))
PI = 3.14
print(f"P = {2*Radius*PI} , S = {PI*pow(Radius,2)}")