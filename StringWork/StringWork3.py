String = input("Please enter a string : ")
Char = input("Please enter a character : ")

def CheckString(String):
    while(not String.isalpha()) :
        String = input("Please enter a string : ")

    return String

def CheckChar(Char) :
    while(len(Char) != 1 or not Char.isalpha()) :
        Char = input("Please enter a character : ")

    return Char

String = CheckString(String)
Char = CheckChar(Char)


for char in range(len(String)) :
    if(Char.lower() == String[char].lower()) :
        print(char)
        break

else :
    print(-1)