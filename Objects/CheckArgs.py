String = input("Please enter a string of sort: ")



def ReverseString(sTR) :
    if(len(sTR) == 1) :
        return sTR
    else :
        return sTR[len(sTR)-1] + ReverseString(sTR[0:(len(sTR)-1)])



print(ReverseString(String))