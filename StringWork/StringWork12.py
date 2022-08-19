
SequenceString = input("Please enter a Sequance of string : ")
SequenceString= SequenceString.capitalize()

for i in range(len(SequenceString)) :
    if(SequenceString[i] == " " or SequenceString[i] == "," or SequenceString[i] == ".") :
        SequenceString = SequenceString[:i+1] + SequenceString[i+1].capitalize() + SequenceString[i+2:]

print(SequenceString)