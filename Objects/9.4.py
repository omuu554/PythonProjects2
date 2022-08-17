import datetime

Num = input("Please enter a number between 1-7: ")
#DayDateToday = datetime.datetime.now().date() - datetime.timedelta(days= 1)
WeekDayDateToday = datetime.datetime.now().isoweekday() + 1
DeltaTodayAndNum = 0



while(not Num.isdigit() or int(Num) < 1 or int(Num) > 7) :
    Num = input("Please enter a CORRECT number between 1-7: ")

DeltaTodayAndNum = (datetime.datetime.now().isoweekday() + 1) - int(Num)
if(DeltaTodayAndNum > 0) :
    DayDateToday = datetime.datetime.now().date() - datetime.timedelta(days=DeltaTodayAndNum)

elif(DeltaTodayAndNum < 0) :
    DeltaTodayAndNum = abs(DeltaTodayAndNum)
    DayDateToday = datetime.datetime.now().date() - datetime.timedelta(days=DeltaTodayAndNum)

else :
    DayDateToday = datetime.datetime.now().date()


print("The day that was chosen is:",DayDateToday.strftime("%A"), ",and the date today is:",DayDateToday.strftime("%d/%m/%y"))