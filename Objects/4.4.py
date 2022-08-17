List1 = []
List2 = []
ListNumAmount1 = int(input("Please enter the amount of things in the first list: "))
ListNumAmount2 = int(input("Please enter the amount of things in the second list: "))

for i1 in range(ListNumAmount1) :
    Num = input("Please enter the thing to enter to the first list: ")
    List1.append(Num)

for i2 in range(ListNumAmount2) :
    Num = input("Please enter the thing to enter to the second list: ")
    List2.append(Num)

ListMerge = List1 + List2
print(f"The List {ListMerge} length is {len(ListMerge)}")