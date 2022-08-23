
SequenceString = input("Please enter a Sequance of string : ")
String = input("Please enter a string : ")
Words = SequenceString.split(' ')
Index = 0
#count = 0

ListIndexes = []



for Strings in Words :
    if(String == Strings) :
      for i in range(len(String)):
        # if(count == 0):
         ListIndexes.append(Index)
          #count +=1

         if(i == len(String)-1):
            Index += 2
         else:
             Index += 1

      #count = 0

    else :
        Index += len(Strings)+1


print(ListIndexes)


