import random

List = []
NewList = []

for i in range(50) :
    Num = random.randint(1,10)
    List.append(Num)

for i in List:
    if(i not in NewList ):
        NewList.append(i)


print(List)
print(NewList)

