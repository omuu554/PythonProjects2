import random

List = []
NewList = []

for i in range(10) :
    Num = random.randint(0,100)
    List.append(Num)

print(List)
NewList = List[0:5]
print(NewList)

