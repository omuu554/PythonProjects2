from random import randint

def InvalidNum(Num):
     while(not Num.isdigit()):
         Num = input("Please enter a correct digit: ")

     return Num

def CountInList(List, Num):
    Count = 0
    for Numbers in List:
        if(Numbers == int(Num)):
            Count += 1

    return Count

def RandomNums(List):
    List.clear()
    for Numbers in range(20):
        List.append(randint(1,100))


List = []
RandomNums(List)
Num = input("Please enter a number: ")
Num = InvalidNum(Num)
print(f"The number {Num} is shown {CountInList(List,Num)} in the list: {List}")
