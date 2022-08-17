ListOfNumbers = []
global FakeList2
FakeList2 = []

def CreateList(ListNum) :
    StopLoop = "No"
    while(StopLoop != ""):
     Num = int(input("Please enter a number to the list: "))
     ListNum.append(Num)
     StopLoop = input("Please enter ("") if you want to stop: ")

def UniqeNumbers1(ListNum) :
    ListNum = sorted(set(ListNum), key=ListNum.index)
    return list(ListNum)

def UniqeNumbers2(ListNum) :
   FakeListNum = []
   for Numbers in range(len(ListNum)) :
       if(ListNum[Numbers] not in FakeListNum) :
           FakeListNum.append(ListNum[Numbers])

   return FakeListNum

CreateList(ListOfNumbers)
print(UniqeNumbers2(ListOfNumbers))
print(UniqeNumbers1(ListOfNumbers))
