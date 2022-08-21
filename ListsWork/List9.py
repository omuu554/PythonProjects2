import random

List = []
NewList = []
NumUser = int(input("Please enter a number to be added to the list: "))

for i in range(10) :
    Num = random.randint(1,10)
    List.append(Num)

NewList = List[6::-1]
NewList.append(NumUser)
print(List)
print(NewList)

