import datetime
import re

BirthYear = input("Please enter a birth Year: ")

BirthMonth = input("Please enter a birth month(Jan - Dec): ")
BirthMonth = re.sub('\s+', '', BirthMonth)
BirthMonthsAllowed = re.compile("Jan|Feb|Mar|Apr|May|June|July|Aug|Sept|Oct|Nov|Dec")

BirthDay = input("Please enter a birthday (1-31): ")

BirthDate = ""
DateTimeBirthDate = ""

while(not BirthYear.isdigit()) :
    BirthYear = input("Please enter REALISTIC BIRTH YEAR: ")

while(not re.match(BirthMonthsAllowed,BirthMonth)) :
    BirthMonth = input("Please enter a CORRECT birth month(Jan - Dec)!!!!: ")
    BirthMonth = re.sub('\s+', '', BirthMonth)

while(not BirthDay.isdigit() or int(BirthDay) < 1 or int(BirthDay) > 31) :
    BirthDay = input("Please enter a REALISTIC birthday (1-31): ")

BirthDate = BirthDay + "/" + BirthMonth + "/" + BirthYear
print(BirthDate)
DateTimeBirthDate = datetime.datetime.strptime(BirthDate,'%d/%b/%Y').date()
print(DateTimeBirthDate)