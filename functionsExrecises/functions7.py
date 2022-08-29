
def GetMaxNumber(Num1, Num2):
    if(Num1 >= Num2):
        return Num1
    else :
        return Num2

def GetMinNumber(Num1, Num2):
    if(Num1 <= Num2):
        return Num1
    else :
        return Num2

def PrintNumbersBetween(Num1, Num2):
    for Numbers in range(GetMinNumber(Num1,Num2), GetMaxNumber(Num1,Num2) + 1):
        print(Numbers, end= " ")


Number1 = int(input("Please enter a number: "))
Number2 = int(input("Please enter a second number: "))
PrintNumbersBetween(Number1,Number2)