

def FindNum(NumList:list,Num,staringIndex = 0):
    Index = 0

    for i in range(staringIndex,len(NumList)):
        if(NumList[i] == Num):
            Index = i
            break

    return Index



List = [12,5,4,6,88,9,2,3,4,4,2,21,34,22,78,32,2,21,32,54,767,15]
Num = 4
startingIndex = 3
print(FindNum(List,Num,startingIndex))
