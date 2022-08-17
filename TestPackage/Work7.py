Num = int(input("Please enter a number: "))

if Num >= 10 and Num <= 100 :
    if Num%7 == 0 or Num%10 == 7 or Num // 10 == 7 :
        print("Lucky Number")
    else :
        print("Unlucky Number")
else :
    print("Error Number")