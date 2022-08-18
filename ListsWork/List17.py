import random

List = []
List2 = []

for i in range(5) :
    Num = random.randint(0,100)
    Num2 = random.randint(0,100)
    List.append(Num)
    List2.append(Num2)

for i in List:
    if (i in List2) :
        print("Found it")
        break

else :
    print("Not Found")

print(List)
print(List2)