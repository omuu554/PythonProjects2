String = input("Please enter a string : ")

def CheckString(String):
    while(not String.isalpha()) :
        String = input("Please enter a string : ")

    return String

String = CheckString(String)
LastAndFirst = String[0] + String[len(String) - 1]

for Char in range(len(String)) :
    print(LastAndFirst)