import random

List = []
ListDiv3 = []
ListUnDiv3 = []

for i in range(10) :
    Num = random.randint(1,10)
    List.append(Num)

for i in List :
    if(i % 3 == 0) :
        ListDiv3.append(i)
    else :
        ListUnDiv3.append(i)

print(List)
print(ListDiv3)
print(ListUnDiv3)

