NumUser = int(input("Please enter a number: "))
Deviders = 1

ListDividers = []

while(NumUser != Deviders) :
    if(NumUser % Deviders == 0) :
        ListDividers.append(Deviders)
    Deviders += 1

print(ListDividers)