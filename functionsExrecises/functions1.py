
def CheckIfNum3Digits(Num):
    Num = abs(Num)
    while(Num < 100 or Num > 999):
        Num = int(input("Please enter a new correct num: "))
    return Num

def Sum3Digit(Num):
    Num = CheckIfNum3Digits(Num)
    return (Num % 10) + (Num // 10 %10) + (Num // 100)

Number = int(input("Please enter a 3 digit number: "))

print(Sum3Digit(Number))