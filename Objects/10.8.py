Num = int(input("Please enter a number bigger than 1: "))
StaticNum = 0

def NumInit(Num,StaticNum) :
    while(Num < 1) :
        Num = int(input("Please enter a number bigger than 1: "))
    StaticNum = Num
    Num = Num - 1
    return Num,StaticNum

def IsPrimeNumber2(Num) :
    for Numbers in range(2,Num) :
        if(Num % 2 == 0 ) :
            return False
            break
    else :
        return True

def IsPrimeNumber(Num,FakeNum) :
    global Start
    Start = 1

    if(Num == Start) :
        return True
    else :
        if(FakeNum % Num == 0) :
         return False & IsPrimeNumber(Num - 1,FakeNum)
        else :
         return True & IsPrimeNumber(Num - 1,FakeNum)

Num,StaticNum = NumInit(Num,StaticNum)
#print(IsPrimeNumber(Num,StaticNum))
print(IsPrimeNumber2(StaticNum))

