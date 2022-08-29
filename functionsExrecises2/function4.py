


def MaxNumInList(*NumList):
    MaxNum = -9999999999
    for Num in NumList[0]:
         if(MaxNum < Num):
            MaxNum = int(Num)


    return MaxNum



List = [12,5,4,6,88,9,2,3,4,4,2,21,34,22,78,32,2,21,32,54,767,15]
print(MaxNumInList(List))
