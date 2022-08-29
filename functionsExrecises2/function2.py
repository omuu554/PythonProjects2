

def NumInList(NumList:list,Num):
    count = 0
    FakeList = NumList.copy()
    while(Num in FakeList):
        FakeList.remove(Num)
        count +=1

    return count


List = [12,5,4,6,88,9,2,3,4,4,2,21,34,22,78,32,2,21,32,54,767,15]
Num = 55
print(NumInList(List,Num))