ListOfNumbers = []


def CreateList(ListNum) :
    StopLoop = "No"
    while(StopLoop != ""):
     Num = int(input("Please enter a number to the list: "))
     ListNum.append(Num)
     StopLoop = input("Please enter ("") if you want to stop: ")

def MultiplyList(ListNum) :
    Sum = 1
    for Numbers in ListNum :
        Sum += ListNum

    return Sum



CreateList(ListOfNumbers)
print(MultiplyList(ListOfNumbers))