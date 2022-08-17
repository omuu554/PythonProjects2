UserNum = int(input("Please enter Dictinary size: "))
UserAbsNum = abs(UserNum)
DicNum = {}
DicNum2 = {}

NumDown = 1

for Numbers in range(UserAbsNum) :

   if(UserNum > 0) :
    NumModified = Numbers + 1
   else :
       NumModified = Numbers - NumDown
       NumDown += 2
   DicSlot = {NumModified: NumModified * NumModified}
   DicNum2 = DicNum2 | DicSlot
   DicNum.update(DicSlot)


print(DicNum)
print(DicNum2)