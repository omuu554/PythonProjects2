import random

NumUser = int(input("Please enter a number: "))
NumList = []
NumTuple = ()
NewNumTuple = ()

for numbers in range(10) :
    Num = random.randrange(1, 101)
    NumList.append(Num)

NumTuple = tuple(NumList)
NewNumTuple = (NumTuple[6:10]+NumTuple[0:4])
NumTuple = list(NumTuple)
NumTuple.append(NumUser)
NumTuple = tuple(NumTuple)
print(NumTuple)
NewNumTuple = list(NewNumTuple)
NewNumTuple.pop(0)
NewNumTuple = tuple(NewNumTuple)
print(NewNumTuple)