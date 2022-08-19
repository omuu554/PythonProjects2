
SequenceString = input("Please enter a Sequance of string : ")
String = input("Please enter a string : ")
Words = SequenceString.split(' ')
Index = 0

ListIndexes = []

for Strings in Words :
    if(String == Strings) :
        for i in range(len(String)):
            ListIndexes.append(Index)
            Index += 1
    else :
        Index += len(Strings)


print(ListIndexes)

