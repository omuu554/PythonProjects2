import re

MaxNum = 0
MinNum = 0
IsBreak = False
Set1 = set()
Set2 = set()
Set3 = set()
Set4 = set()
AddToSet2 = ""

num = input("Please enter a number for the first list: ")

while(num != "" ) :
    while (not num.isdigit()):
        num = input("Please enter a fucking number: ")
        if (num == ""):
            IsBreak = True
            break

    if (IsBreak):
        IsBreak = False
        break

    Set1.add(int(num))

    AddToSet2 = input("Please enter if you want to add the number to set2(Y/N): ")

    while(AddToSet2 != "N" and AddToSet2 != "Y" ) :
        AddToSet2 = input("Please enter if you want to add the number to set2(Y/N): ")

    if(AddToSet2 == "Y") :
        Set2.add(int(num))
    else:
        print("The number was not added")

    num = input("Please enter a number for the first list: ")

num = input("Please enter a number for the second list : ")

while(num != "" ) :
    while (not num.isdigit()):
        num = input("Please enter a fucking number: ")
        if(num == "") :
            IsBreak = True
            break
    if(IsBreak) :
        IsBreak = False
        break
    Set2.add(int(num))
    num = input("Please enter a number for the second list: ")

print(Set1, Set2)
Set3.update(Set1,Set2)
print(Set3)
Set1 = list(Set1)
if(len(Set1) > 0) :
 Set1.pop(0)
Set1 =set(sorted(set(Set1) , key= Set1.index))


print(Set1)

for Elements in Set3 :
    MaxNum = max(Elements, MaxNum)
    MinNum = min(Elements, MaxNum)

Set1.clear()
Set2.clear()
Set4 = Set3.copy()
num = input("Please enter a number for the forth list: ")
while(num != "" ) :
   while(not num.isdigit()):
       num = input("Please enter a fucking number: ")
       if (num == ""):
           IsBreak = True
           break

   if (IsBreak):
      IsBreak = False
      break

   Set4.add(int(num))

   num = input("Please enter a number for the forth list: ")

print(f"The new set is {len(Set3)} elements long and its max number is {MaxNum} , and the minimum number is {MinNum}")
print(Set4)


