

class Person:
    def __init__(self, Name, Age,ChildrenAmount = 0):
        self.Name = Name
        self.Age = int(Age)
        self.ChildAmount = int(ChildrenAmount)
        self.FixName()
        self.FixAge()
        self.FixChildren()

    def FixName(self):
        while(self.Name == "" or not self.Name.isalpha()):
            Name = input("Please enter a good Name: ")
            self.SetName(Name)

    def FixChildren(self):
        while(self.ChildAmount < 0 ):
            Amount = int(input("Please enter a good amout of children: "))
            self.SetChildren(Amount)

    def FixAge(self):
        while(self.Age <= 0):
            Age = int(input("Please enter a good Age(> 0): "))
            self.SetAge(Age)

    def SetName(self,Name):
        self.Name = Name

    def SetAge(self, Age):
        self.Age = Age

    def SetChildren(self,Children):
        self.ChildAmount = Children

    def Show(self):
        print(f"{self.Name} is {self.Age} year and old and he has {self.ChildAmount} Children")

    def HasChildren(self):
        return self.ChildAmount > 0

    def AgeGroup(self):
        if(self.Age <= 18 ):
            return "Child"
        if (self.Age >= 19 and self.Age <=60):
            return "Adult"
        if (self.Age >= 61 and self.Age <= 120):
            return "Senior"
        else :
            return "World Record"
