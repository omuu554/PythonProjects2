import random

List = []
Last3List = []

for i in range(10) :
    Num = random.randint(1,10)
    List.append(Num)

Last3List = List[len(List)-3:]
print(List)
print(Last3List)


