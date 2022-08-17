ListOfNumbers = []

def SumOfNumber(ListNum) :
    if(len(ListNum) == 1) :
        if(ListNum[0] % 2 == 0) :
            return ListNum[0]
        else :
            return 0
    else :
        if(ListNum[len(ListNum)-1] % 2 == 0) :
            return ListNum[len(ListNum)-1] + SumOfNumber(ListNum[0:len(ListNum)-1])
        else :
            return  SumOfNumber(ListNum[0:len(ListNum)-1])

def SumOfNumber2(ListNum) :
    Sum = 0
    for Numbers in ListNum :
        if(Numbers % 2 == 0):
            Sum += Numbers

    return Sum

def CreateList(ListNum) :
    StopLoop = "No"
    while(StopLoop != ""):
     Num = int(input("Please enter a number to the list: "))
     ListNum.append(Num)
     StopLoop = input("Please enter ("") if you want to stop: ")

CreateList(ListOfNumbers)

print(SumOfNumber(ListOfNumbers))
print(SumOfNumber2(ListOfNumbers))

