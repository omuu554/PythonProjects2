UserNum = int(input("Please enter Dictinary size: "))
UserAbsNum = abs(UserNum)
UserKeyFind = int(input("Please enter Dictinary Key: "))
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
   DicNum.update(DicSlot)


DicNum.pop(UserKeyFind)
"""for KeyNumbers,ValueNumbers in DicNum.items() :
    if(UserKeyFind != KeyNumbers) :
       DicSlot ={KeyNumbers:ValueNumbers}

    DicNum2.update(DicSlot)

DicNum = DicNum2"""
print(DicNum)