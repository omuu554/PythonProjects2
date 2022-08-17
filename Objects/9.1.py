import datetime

Name = input("Please enter a name: ")
Age = int(input("Please enter an age: "))
YearsUntil100 = 100 - Age
YearWhen100old = datetime.datetime.now() + datetime.timedelta(weeks= YearsUntil100*52)
YearWhen100oldString = YearWhen100old.strftime("%d/%m/%y")
print(f"The year is {YearWhen100old.year} and the date is {YearWhen100old.date()} and it look better in this {YearWhen100oldString}")
print("He became older")


