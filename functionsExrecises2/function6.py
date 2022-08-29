

def RemoveElement(List:list, Element):
    for i in range(len(List)):
        if(List[i] == Element):
            del List[i]
            break


List = [12,5,4,6,88,9,2,3,4,4,2,21,34,22,78,32,2,21,32,54,767,15]
Num = 4
RemoveElement(List, Num)
print(List)