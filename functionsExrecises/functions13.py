from random import randint

def InvalidNum(Num):
     while(not Num.isdigit()):
         Num = input("Please enter a correct digit: ")

     return Num

def getMaxInList(List):
    MaxNum = 0
    MaxNumIndex = 0
    for Numbers in range(len(List)):
        if(List[Numbers] >= MaxNum):
            MaxNumIndex = Numbers
            MaxNum = List[Numbers]

    return MaxNumIndex,MaxNum

def RandomNums(List):
    List.clear()
    for Numbers in range(20):
        List.append(randint(1,100))


List = []
RandomNums(List)
MaxNumIndex,Num = getMaxInList(List)
print(f"The number {Num} is shown in index {MaxNumIndex} in the list: {List}")
