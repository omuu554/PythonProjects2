import random

List = ["Apple","Dog", "Big","New","World","Power","Missipi","Arnold","Whisky","Butter","Money","Gold","Israel","Oriel","Bible","Natan","Electric","Game","Home","House","Banana","Meat","Row","Find","Destroy","Ball","Pear","Door"]
ComputerString = random.choice(List)
UserGuess = ""
RevealWord = "_"

CountGuesses = 0
for i in range(len(ComputerString)-1):
    RevealWord = RevealWord+"_"

print(ComputerString)
print("Please Guess the word:")
print(RevealWord)

def FixUserGuess(UserGuess) :
    while (len(UserGuess) > 1 or UserGuess == "" or not UserGuess.isalpha()):
        UserGuess = input("Please guess a char: ")

    return UserGuess


while(CountGuesses != 8) :
    if(RevealWord == ComputerString):
        print(f"Congrats you found the word {ComputerString}!!!")
        break

    UserGuess = FixUserGuess(UserGuess)
    for i in range(len(ComputerString)) :
        if(UserGuess == ComputerString[i].lower()):
            RevealWord = RevealWord[:i] + ComputerString[i] + RevealWord[i+1:]

    print(f"The word is now {RevealWord}")
    CountGuesses += 1
    UserGuess = ""
else :
    print(f"You have failed to find the word {ComputerString} :(")



