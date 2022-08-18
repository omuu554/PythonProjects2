import random

List = []
count = 0

for i in range(10) :
    Num = random.randint(0,100)
    List.append(Num)

for i in List:
    print(f"The number {i} is shown: {List.count(i)}")

for i in List:
    print(f"The Number {i} is shown:",end= "")
    for x in List :
        if i == x :
            count += 1
    print(f"{count} times", end= '\n')
    count = 0


print(List)

