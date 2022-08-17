import re

ListBeforeTuple = []
ListChilrenAge = []
ListAfterTuple = ()

Name = input("Please enter a name: ")
PhoneNumber = input("Please enter a phone number: ")
PhoneNumber = PhoneNumber.replace("-", "")
Age = int(input("Please enter an age: "))
AmountOfChildren = input("Please enter a how much children: ")
ChildrenAge = input("Please enter a the children ages: ")
ListChildrenAge = re.split(',| ,|, | ',ChildrenAge)

while(Name == "") :
 Name = input("Please enter a CORRECT NAME: ")


 while (len(PhoneNumber) < 6 or len(PhoneNumber) > 9) :
  PhoneNumber = input("Please enter a CORRECT PHONE NUMBER: ")
  PhoneNumber = PhoneNumber.replace("-", "")


while(Age < 0) :
    Age = int(input("Please enter a CORRECT AGE: "))

while(int(AmountOfChildren) < 0) :
     AmountOfChildren = input("Please enter a CORRECT AMOUNT OF CHILDREN: ")


while(len(ListChildrenAge) != int(AmountOfChildren) ) :
      ChildrenAge = input("Please enter a THE CORRECT CHILDREN AGES: ")
      ListChildrenAge = re.split(',| ,|, | ', ChildrenAge)


for Ages in range(len(ListChildrenAge)) :
    while(ListChildrenAge[Ages] == "" or int(ListChildrenAge[Ages]) < 0 or ListChildrenAge[Ages].isnumeric() == False) :
        ListChildrenAge[Ages] = input("Please enter a CORRECT AGE: ")



ListBeforeTuple.append(Name)
ListBeforeTuple.append(PhoneNumber)
ListBeforeTuple.append(Age)
ListBeforeTuple.append(AmountOfChildren)
ListBeforeTuple.append(ChildrenAge)

ListAfterTuple = tuple(ListBeforeTuple)
print(ListAfterTuple)
print(f"His name is {ListAfterTuple[0]} and he is {ListAfterTuple[2]} years old\nHis phone number is {ListAfterTuple[1]}\nHe has {ListAfterTuple[3]} children and they are ages {ListAfterTuple[4]}")
