import random

List = []
Last3List = []

for i in range(10) :
    Num = random.randint(1,10)
    List.append(Num)


print(List)
print(List[0::2])