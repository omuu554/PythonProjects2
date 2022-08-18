import random

List = []
NumUser = int(input("Please enter a number: "))


for i in range(20) :
    Num = random.randint(0,100)
    List.append(Num)

while (NumUser in List) :
    List.remove(NumUser)

print(List)

