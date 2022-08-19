

class Bus:
    def __init__(self,MaxSeats):
        self.Seats = int(MaxSeats)
        self.__FixMaxSeats()
        self.Passangers = 0
        self.ListOfSeats = self.__CreateSeats()


    def __str__(self):
        return f"The bus has {self.Seats} and holds {self.Passangers} passangers"

    def __SetPassangers(self,Passangers):
        self.Passangers = Passangers

    def __SetMaxSeats(self,MaxSeats):
        self.Seats = MaxSeats

    def __CreateSeats(self):
        ListOfSeats = []
        for seats in range(self.Seats) :
            ListOfSeats.append("Free")
        return ListOfSeats

    def __FixMaxSeats(self):
        while(self.Seats <= 0) :
            MaxSeats = int(input("Please enter amount of seats in the bus: "))
            self.__SetMaxSeats(MaxSeats)


    def getOn(self, PassangerName):
        while(not PassangerName.isalpha()) :
            PassangerName = input("Please enter a correct name: ")
        for Seats in range(len(self.ListOfSeats)) :
            if (self.ListOfSeats[Seats] == "Free") :
                self.ListOfSeats[Seats] = PassangerName
                self.__SetPassangers(self.Passangers + 1)
                break

        else :
            print(f"The Buss is full, {PassangerName.capitalize()} didn't go on the bus ")

    def getOff(self, PassangerName):
        while (not PassangerName.isalpha()):
            PassangerName = input("Please enter a correct name: ")
        for Seats in range(len(self.ListOfSeats)) :
            if(self.ListOfSeats[Seats].lower() == PassangerName.lower()) :
                self.ListOfSeats[Seats] = "Free"
                self.__SetPassangers(self.Passangers - 1)
                break
        else :
            print(f"The passanger {PassangerName} was not found on the bus")


