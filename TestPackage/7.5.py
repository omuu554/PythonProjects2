UserNum = int(input("Please enter Dictinary size: "))
UserAbsNum = abs(UserNum)
DicNum = {}
SumOfValue = 0


NumDown = 1

for Numbers in range(UserAbsNum) :
   if(UserNum > 0) :
    NumModified = Numbers + 1
   else :
       NumModified = Numbers - NumDown
       NumDown += 2

   DicSlot = {NumModified: NumModified * NumModified}
   DicNum.update(DicSlot)

for SumNum in DicNum.values() :
    SumOfValue += SumNum

print(f"The sum of all the values is: {SumOfValue}")