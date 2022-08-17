Sentence = input("Please enter a Sentence: ")
Char = input("Pleae enter a character: ")
CharAmount = 0

while len(Char) != 1 :
    print("The Char length is supposed to be one please enter a new character")
    Char = input("Pleae enter a character: ")


if Char in Sentence:
     for x in range(len(Sentence)):
        if Sentence[x] == Char:
             CharAmount += 1
else :
    print("Char doesn't exist in the sentence")

print(f"The character {Char} is show {CharAmount} times.")