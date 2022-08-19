SequenceString = input("Please enter a Sequance of string : ")
Char = input("Please enter a character : ")

def CheckChar(Char) :
    while(len(Char) != 1) :
        Char = input("Please enter a character : ")

    return Char

Char = CheckChar(Char)

for i in range(len(SequenceString)) :
    if(Char == SequenceString[i]) :
        SequenceString = SequenceString[:i] + SequenceString[i].capitalize() + SequenceString[i+1:]

print(SequenceString)