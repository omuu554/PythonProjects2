ListOfNumbers = []

def SumNum(ListNum):

    if(len(ListNum) == 1) :
        return ListNum[0]
    else :
        return ListNum[len(ListNum)-1] + SumNum(ListNum[0:len(ListNum)-1])


def CreateList(ListNum) :
    StopLoop = "No"
    while(StopLoop != ""):
     Num = int(input("Please enter a number to the list: "))
     ListNum.append(Num)
     StopLoop = input("Please enter ("") if you want to stop: ")



CreateList(ListOfNumbers)
print(SumNum(ListOfNumbers))