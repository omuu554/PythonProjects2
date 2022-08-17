Day = int(input("Please enter a day: "))
Month = int(input("Please enter a month: "))
Year = int(input("Please enter a year: "))
YearIsWrong = False #YearIsWrong = 0
MonthIsWrong = False #MonthIsWrong = 0
DayIsWrong = False #DayIsWrong = 0
StringYearIsWrong = "Unuasble Year"
StringMonthIsWrong = "Unuasble Month"
StringDayIsWrong = "Unuasble Day"


if Year >= 1950 and Year <= 2020 and Month >= 1 and Month <= 12 and Day >= 1 and Day <= 31 :
     if Month == 2 and Day > 28 or Month == 4 and Day > 30 or Month ==6 and Day > 30 or Month == 8 and Day > 30 or Month == 10 and Day > 30 or Month == 12 and Day > 30 :
         print(StringDayIsWrong)
     else :
         print(f"{Day % 100 // 10}{Day % 10}/{Month % 100 // 10}{Month % 10}/{Year % 100}")
else :
    if Year < 1950 or Year > 2020 :
        print(StringYearIsWrong)
    if Month < 1 or Month > 12 :
        print(StringMonthIsWrong)
    if Day < 1 or Day > 31 :
        print(StringDayIsWrong)



"""if Year < 1950 or Year > 2020 :
    YearIsWrong = True #YearIsWrong = 1
if Month < 1 or Month > 12:
    MonthIsWrong = True  #MonthIsWrong = 1
if Day < 1 or Day > 31 :
    DayIsWrong = True #DayIsWrong = 1
else :
    if Month == 2 and Day > 28 or Month == 4 and Day > 30 or Month ==6 and Day > 30 or Month == 8 and Day > 30 or Month == 10 and Day > 30 or Month == 12 and Day > 30  :
        DayIsWrong = True  # DayIsWrong = 1


if YearIsWrong  : #YearIsWrong == 1
    print(f"{StringYearIsWrong}")
    if MonthIsWrong :#MonthIsWrong == 1
        print(f"{StringMonthIsWrong}")
        if DayIsWrong :#DayIsWrong == 1
            print(f"{StringDayIsWrong}")
    else :
        if DayIsWrong :#DayIsWrong == 1
            print(f"{StringDayIsWrong}")

else :
    if MonthIsWrong : #MonthIsWrong == 1
        print(f"{StringMonthIsWrong}")
        if DayIsWrong :#DayIsWrong == 1
            print(f"{StringDayIsWrong}")
    else :
        if DayIsWrong :#DayIsWrong == 1
            print(f"{StringDayIsWrong}")
        else :
            print(f"{Day%100//10}{Day%10}/{Month%100//10}{Month%10}/{Year % 100}")"""


"""if Year >= 1950 and Year <= 2020 :
    if Month >= 1 and Month <= 12 :
        if Day >= 1 and Day <= 31 :
            print(f"{Day}/{Month}/{Year%100}")
        else :
           print("Date Is Not Allowed!!!!!! \nPlease Change it")
    else :
        print("Month Is Not Allowed!!!!!! \nPlease Change it")
else :
    print("Year Is Not Allowed!!!!!! \nPlease Change it")"""


"""if Year >= 1950 and Year <= 2020 and  Month >= 1 and Month <= 12 and Day >= 1 and Day <= 31 :
    print(f"{Day}/{Month}/{Year % 100}")
else :
    print("Error")"""



