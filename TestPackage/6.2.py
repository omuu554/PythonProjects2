ListBeforeTuple = []
ListAfterTuple = ()
CharCount = 5
StringFromTuple = ""

while(CharCount != 0) :
    Char = input("Please enter a single character: ")
    if(len(Char) == 1) :
        CharCount -= 1
        ListBeforeTuple.append(Char)
    else :
        print("Please enter a correct character!!!!!")

ListAfterTuple = tuple(ListBeforeTuple)
for Chars in ListAfterTuple :
    StringFromTuple += Chars

print(f"The word we created is: {StringFromTuple}")

