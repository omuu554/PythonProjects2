import random

List = []
Num2 = random.randint(1,10)

for i in range(10) :
    Num = random.randint(1,10)
    List.append(Num)

print(Num2)
print(List)

for i in range(10) :
    if(List[i] == Num2) :
        print(i)
        break
else :
    print("It wasnt found")
