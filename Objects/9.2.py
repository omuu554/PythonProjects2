import datetime

DateEuro = datetime.datetime.now().strftime("%d/%m/%y")
DateUSA = datetime.datetime.now().strftime("%m/%d/%y")
print(f"Date today in the europe is {DateEuro} and in the usa its shown {DateUSA} ")
print( datetime.datetime.now().strftime("%d/%m/%y"), datetime.datetime.now().strftime("%m/%d/%y"))

