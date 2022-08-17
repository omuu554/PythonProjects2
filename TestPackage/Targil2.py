#תרגיל 2
Day = input("Please enter the day:")
if int(Day) <= 31 and int(Day) > 0 :
    Month = input("Please enter the month:")
    if int(Month) <= 12 and int(Month) > 0 :
        Year = input("Please enter the year:")
        print(f"{int(Day)%100//10}{int(Day)%10} / {int(Month)%100//10}{int(Month)%10} / {int(Year)%100//10}{int(Year)%10}")
    else :
        print("Please enter a good month")
else:
    print("Please enter a good day")
