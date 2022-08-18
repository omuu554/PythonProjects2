import re

class Student:
    def __init__(self, Name, IDNumber, Grade = 0):
        "creates a student with a name and id number and a grade"
        self.name = Name
        self.id = int(IDNumber)
        self.grade = int(Grade)
        self.FixID()
        self.FixGrade()


    def FixID(self):
        IDAllowed = re.compile('\d{9}')
        while(not IDAllowed.match(str(self.id))) :
            id = int(input("Please enter a Valid id: "))
            self.SetId(id)

    def FixGrade(self):
        while(self.grade < 0 or self.grade > 100) :
            NewGrade = int(input("Please enter a Valid grade: "))
            self.SetGrade(NewGrade)

    def SetId(self, Id):
        self.id = Id

    def SetGrade(self,Grade):
        self.grade = Grade

    def CheckPass(self):
        return self.grade>=70

    def UpdateGrade(self,Precentage):
        Precentage = int(Precentage)
        NewGrade = self.grade + (self.grade*Precentage/100)
        if(NewGrade > 100 ) :
            NewGrade == 100
        self.SetGrade(NewGrade)
        return NewGrade

    def Show(self):
        print(f"{self.name.capitalize()} is a student, His id is {self.id} and his grade is {self.grade} ")


