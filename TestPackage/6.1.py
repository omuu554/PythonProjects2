ListBeforeTuple = []
ListAfterTuple = ()

for x in range(3) :
    Num = int(input("Please enter a number to be added to Tuple: "))
    ListBeforeTuple.append(Num)

ListAfterTuple = tuple(ListBeforeTuple)
(a, b, c) = ListAfterTuple
print(f"The Tuple has the numbers {a}, {b}, {c}")