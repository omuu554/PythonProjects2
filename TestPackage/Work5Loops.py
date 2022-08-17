Num = int(input("Please enter a number: "))

while(Num >= 10 and Num <= 99) :
    if(Num % 7 == 0 or Num // 10 == 7 or Num % 10 == 7 ) :
        print("You chose a lucky Number")
    else :
        print("You chose a unlucky Number")

    Num = int(input("Please enter a number: "))

print("Error the Number you chose does not meet the criteria!!!!!!!!!!!!!")
