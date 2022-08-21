String = input("Please enter a string : ")

def CheckString(String):
    while(not String.isalpha()) :
        String = input("Please enter a string : ")

    return String

String = CheckString(String)


String =String.replace('a' , '')
String = String.replace('A', '')
print(String)

for Char in range(len(String)):
    if(Char == len(String) - 1):
        break
    if(String[Char] == 'a' or String[Char] == 'A') :
        String = String[:Char] + String[Char + 1 :]

if(String[len(String)-1] == 'a' or String[len(String)-1] == 'A') :
    String = String[:len(String)- 2]

print(String)