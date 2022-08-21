x = open("Story.txt", 'w')
x.write("A boy is playing there.\nThere is a playground.\nAn airplane is in the sky.\nThe sky is pink\nAlphabet and numbers are allowed in the password")
x.close()
count = 0
Count2 = 0

def CountWords(File) :
    count = 0
    for Line in File :
        count += 1

    return count



with open("Story.txt", 'r+') as File:
    for Line in File :
        if (Line[0] != "T"):
            count += 1

    File.seek(0)
    for Line in File :
        Words = Line.split()
        for Word in Words:
            if(Word == "The" or Word == "the"):
                Count2 += 1

    File.seek(0)
    Count3 = CountWords(File)

    File.close()


print(count)
print(Count2)
print(Count3)
