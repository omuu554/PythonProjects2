ListOfNumbers = [1, 2, 3, 4, 5, 6 , 7, 8 ,9, 10]
NewOddListOfNumbers = []
ListOfNumbersX2 = []
Last3List = ListOfNumbers[7:10]
LastAndFirstListOfNumber = [ListOfNumbers[0], ListOfNumbers[len(ListOfNumbers)-1]]

Num1 = int(input("Please enter the first number: "))
Num2 = int(input("Please enter the second number: "))
Num3 = int(input("Please enter the third number: "))

print(LastAndFirstListOfNumber)#g
print(Last3List[::-1])#a
for i in range(len(ListOfNumbers)) :
   if i%2 == 0 :
       print(f"{ListOfNumbers[i]},", end= '')#b

for x in ListOfNumbers :
    ListOfNumbersX2.append(x*2)

print(f"\n{ListOfNumbersX2}")#f

for j in ListOfNumbers :
    if j%2 != 0 :
        NewOddListOfNumbers.append(j)

print(f"\n{NewOddListOfNumbers}")#d

ListOfNumbers[4] = Num1 ; ListOfNumbers[5] = Num2 ; ListOfNumbers.append(Num3)
print(ListOfNumbers)#e

