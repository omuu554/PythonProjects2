String = input("Please enter a string : ")
Char = input("Please enter a character : ")
Count = 0

def CheckString(String):
    while(not String.isalpha()) :
        String = input("Please enter a string : ")

    return String

def CheckChar(Char) :
    while(len(Char) != 1) :
        Char = input("Please enter a character : ")

    return Char

String = CheckString(String)
Char = CheckChar(Char)

for i in range(len(String)) :
    if(String[i].lower() == Char.lower()) :
        Count += 1

print(Count)