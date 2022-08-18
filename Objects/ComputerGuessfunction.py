import random
import re

global UserAnswer
global ComputerNum

MaxRange = 100
MinRange = 1
ComputerGuess = 1

UserNum = int(input("Please enter a number: "))
ComputerNum = random.randint(MinRange , MaxRange)
print(f"Computer number is {ComputerNum}")
UserAnswer = input("Please tell the computer if it (l,h,c): ")


def IsAnswerGood(UserAnswer) :
    AllowedAnswer = re.compile("c|l|h")
    while( not AllowedAnswer.match(UserAnswer)) :
        UserAnswer = input("Please tell the computer if it (l,h,c): ")

    return UserAnswer

def IsEqual(UserNum, ComputerNum) :
    return UserNum == ComputerNum

def IsUserAndNumberEqual(UserNum, ComputerNum,UserAnswer) :
   if(IsEqual(UserNum, ComputerNum) and UserAnswer != 'c') :
       print("Dont Try to fool me enter C")
       while(UserAnswer != 'c') :
           UserAnswer = input("Please enter c : ")
       return False

   elif(not IsEqual(UserNum, ComputerNum) and UserAnswer == 'c'):
       print("STOP TRYING TO STOP THE GAME")
       return True
   else :
       return True


def CheckBigger(UserNum ,ComputerNum ) :
     return UserNum > ComputerNum

def CheckIfBiggerAndInputCorrect(UserNum, ComputerNum, UserAnswer) :
    if(CheckBigger(UserNum, ComputerNum) and UserAnswer == 'h') :
        return 1
    elif( not CheckBigger(UserNum, ComputerNum) and UserAnswer == 'l') :
        return 2
    else :
        return 3

def FixIfIncorrect(UserNum , ComputerNum, UserAnswer) :
    while(CheckIfBiggerAndInputCorrect(UserNum,ComputerNum, UserAnswer) == 3) :
        UserAnswer = input("Please tell the computer if it (l,h,c): ")

    else :
        if(CheckIfBiggerAndInputCorrect(UserNum, ComputerNum, UserAnswer) == 1) :
            return False
        else :
            return True


def RaiseExe(UserNum) :
    if(UserNum < 0 or UserNum > 100) :
        raise ValueError("You did not give a valid number")

RaiseExe(UserNum)
UserAnswer = IsAnswerGood(UserAnswer)
def CheckComputerAnswer(UserNum,ComputerNum,UserAnswer,MaxRange,MinRange,ComputerGuess) :
    while(IsUserAndNumberEqual(UserNum, ComputerNum,UserAnswer)) :
        if(FixIfIncorrect(UserNum,ComputerNum,UserAnswer)) :
            MaxRange = ComputerNum - 1
        else :
            MinRange = ComputerNum + 1

        ComputerNum = random.randint(MinRange,MaxRange)
        print(f"Computer number is {ComputerNum}")
        ComputerGuess += 1
        UserAnswer = input("Please tell the computer if it (l,h,c): ")
        UserAnswer = IsAnswerGood(UserAnswer)

    return ComputerGuess



print(f"It took the computer {CheckComputerAnswer(UserNum, ComputerNum, UserAnswer,MaxRange,MinRange,ComputerGuess)} tries to find the number : {UserNum}")



