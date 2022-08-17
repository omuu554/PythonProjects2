import re

String = input("Please enter a single String: ")
CountA = 0
Counta = 0

def CheckString(String) :
    while(String.isdigit() or not String.isalpha()) and String.islower():
      String = input("Please enter a single String: ")
      String = re.sub('\s+', '', String)

    return String



def CountLowerAndUpper(String,ListaA) :
    if(len(String) == 1) :
        if(String.isupper()) :
            ListaA[1] += 1
            return  ListaA
        elif (String.islower()):
            ListaA[0] += 1
            return ListaA
    else :
        if (String[len(String) -1].isupper()):
            ListaA[1] += 1
            return ListaA + CountLowerAndUpper(String[0:len(String) -1],ListaA)
        elif (String[len(String) -1].islower()):
            ListaA[0] += 1
            return ListaA + CountLowerAndUpper(String[0:len(String) -1],ListaA)





String = CheckString(String)
ListaA = [Counta,CountA ]
ListaA = CountLowerAndUpper(String,ListaA)
print(ListaA[0],ListaA[1])