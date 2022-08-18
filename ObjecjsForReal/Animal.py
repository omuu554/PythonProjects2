
class Animal:
    def __init__(self, Name):
        self.Name = Name
        self.HungerLevel = 5
        self.EnergyLevel = 5

    def __str__(self):
        return f"The animal name is {self.Name}\nHunger Level : {self.HungerLevel}\nEnergy Level : {self.EnergyLevel}"

    def __SetName(self,Name):
        self.Name = Name

    def __SetEnergy(self,Energy):
        self.EnergyLevel = Energy

    def __SetHunger(self,Hunger):
        self.HungerLevel = Hunger

    def FixName(self):
        while(not self.Name.isalpha()):
            Name = input("Please enter a good name for an animal: ")
            self.__SetName(Name)





    def eat(self,GramsFood):
        #HGramsFood = GramsFood/50
        #EGramsFood = GramsFood/100

        while(GramsFood > 0 and self.HungerLevel > 0) :
            if(GramsFood <= 50) :
                self.__SetEnergy(self.EnergyLevel - GramsFood/100)
                self.__SetHunger(self.HungerLevel - GramsFood/50)
                GramsFood = 0
            else :
                self.__SetEnergy(self.EnergyLevel - 50 / 100)
                self.__SetHunger(self.HungerLevel - 50 / 50)
                GramsFood = GramsFood - 50

        if (self.HungerLevel == 0):
            print("The animal is full and wont eat")
        if(self.HungerLevel < 0) :
            print("The animal is full and she didn't finish eating")
            self.__SetHunger(0)
        if (self.EnergyLevel < 0):
            self.__SetEnergy(0)


    def play(self,MinGameTime):

        while (MinGameTime > 0 and self.EnergyLevel > 0):
            if (MinGameTime <= 5):
                self.__SetEnergy(self.EnergyLevel - MinGameTime / 5)
                self.__SetHunger(self.HungerLevel + MinGameTime / 5)
                MinGameTime = 0
            else:
                self.__SetEnergy(self.EnergyLevel - 5 / 5)
                self.__SetHunger(self.HungerLevel + 5 / 5)
                MinGameTime = MinGameTime - 5

        if(self.HungerLevel > 10) :
            self.__SetHunger(10)
        if (self.EnergyLevel == 0):
            print("The animal can't play she doesnt have energy")
            self.__SetEnergy(0)
        if(self.EnergyLevel < 0) :
            print("The game stopped in the middle because the animal is tired")
            self.__SetEnergy(0)


    def rest(self, MinRestTime):
        #EMinRestTime = MinRestTime/20
        #HMinRestTime = MinRestTime/30

        while (MinRestTime > 0 and self.EnergyLevel < 10 and self.HungerLevel < 10 ):
            if (MinRestTime <= 20):
                self.__SetEnergy(self.EnergyLevel + MinRestTime / 20)
                self.__SetHunger(self.HungerLevel + MinRestTime / 30)
                MinRestTime = 0
            else:
                self.__SetEnergy(self.EnergyLevel + 20 / 20)
                self.__SetHunger(self.HungerLevel + 20 / 30)
                MinRestTime = MinRestTime - 20

        #self.__SetHunger(self.HungerLevel + HMinRestTime)
        #self.__SetEnergy(self.EnergyLevel + EMinRestTime)
        if(self.HungerLevel == 10) :
            print("The animal wants to eat, it cant rest")
        if (self.EnergyLevel == 10):
            print("The animal is well rested, it cant rest")
            self.__SetEnergy(10)

        if (self.HungerLevel > 10):
            print("The animal is tired of resting its hungry and wants to eat")
            self.__SetHunger(10)
        if (self.EnergyLevel > 10):
            print("The animal is well rested and wants to play")
            self.__SetEnergy(10)
