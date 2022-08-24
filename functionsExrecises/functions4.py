


def GetSumFromNumber(Num):
    List = range(1, Num + 1 )
    return sum(List)

Number = int(input("Please enter a number: "))

print(GetSumFromNumber(Number))