def CheckIfNum3Digits(Num):
    Num = abs(Num)
    if(Num >= 100 and Num <= 999) :
       print("The number has 3 digits!!!!")
       return True
    else :
        print("The number doesn't have 3 digits!!!!")
        return False


Number = int(input("Please enter a 3 digit number: "))

print(CheckIfNum3Digits(Number))