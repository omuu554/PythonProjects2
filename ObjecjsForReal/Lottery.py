import random

class Lottery:
    def __init__(self, MaxPrize):
        self.__UP = 45
        self.__LOW = 1
        self.__ListOfNumber = self.__RandmonNumbers()
        self.__MaxEarning = self.__SetMaxPrize(MaxPrize)

    def __str__(self):
        return self.__ListOfNumber

    def __RandmonNumbers(self):
        List = []
        for Numbers in range(6):
            Num = random.randint(self.__LOW,self.__UP)
            List.append(Num)

        return List

    def __SetMaxPrize(self,MaxPrize):
        while (not str(MaxPrize).isdigit() or int(MaxPrize) < 0):
            MaxPrize = int(input("Please enter the Max Prize: "))

        return int(MaxPrize)

    def Print(self):
        print(*self.__ListOfNumber, sep = ", ")

    def isNumInList(self, Number):
        while (not str(Number).isdigit() or int(Number) < 0):
            Number = int(input("Please enter a guess: "))
        if (int(Number) in self.__ListOfNumber):
            return True

        return False

    def CorrectGuesses(self, CorrectGusses):
        if(CorrectGusses <= 1) :
            return 0
        elif(CorrectGusses >= 2 and CorrectGusses<= 5) :
            return self.__MaxEarning * CorrectGusses/6

        return self.__MaxEarning
