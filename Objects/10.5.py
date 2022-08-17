

def ChooseMax(Min,Max):
    while(Min > Max) :
        Max = int(input("Please enter a number that will be considered maximum: "))

    return Max

def FindNumber(Num,Min,Max) :
    if(Num == Max ) :
        return True
    elif Max == Min :
        return False
    else :
        return FindNumber(Num,Min,Max-1)

MinNum = int(input("Please enter a number that will be considered minimum: "))

MaxNum = int(input("Please enter a number that will be considered maximum: "))
MaxNum = ChooseMax(MinNum,MaxNum)

Num = int(input("Please enter a number: "))

if(FindNumber(Num, MinNum, MaxNum)) :
    print("The number is between the maximum and minimum")
else :
    print("The number is not between the maximum and minimum")

