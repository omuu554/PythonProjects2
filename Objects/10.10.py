String = input("Please enter a string of sort: ")

def CheckString(String) :
    while(len(String) <= 1) :
        String = input("Please enter a string of sort: ")

    return String


def ReverseString(sTR) :
    if(len(sTR) == 1) :
        return sTR
    else :
        return sTR[len(sTR)-1] + ReverseString(sTR[0:(len(sTR)-1)])

def CheckPlindorum(String) :
    if(String == ReverseString(String)) :
        return True
    else :
        return False

def CheckPlindorum2(String) :
    if(String == ReverseString2(String)) :
        return True
    else :
        return False

def ReverseString2(String) :
    FakeString = ""
    for Char in range(len(String)-1,-1,-1) :
        FakeString += String[Char]
        "".join(FakeString.split())

    return FakeString

def CheckPlindorum3(String) :
    if(len(String) == 1 or len(String) == 0) :
        return True

    return (String[0] == String[len(String)-1]) & CheckPlindorum3(String[1:len(String)-1])

String = CheckString(String)
print(CheckPlindorum(String))
print(CheckPlindorum2(String))
print(CheckPlindorum3(String))