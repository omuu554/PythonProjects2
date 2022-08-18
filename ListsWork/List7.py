import random

List = []
NewList = []

for i in range(10) :
    Num = random.randint(0,100)
    List.append(Num)

print(List)

for i in List :
   if(i % 2 != 0) :
    NewList.append(i)

print(NewList)