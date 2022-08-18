import re


class Course:
    "creates a course that has a name a number an amount of student the got signed for it and the maxiumum amount of students it can hold."
    def __init__(self,NumCourse,NameCourse,MaxSignedStudentsAmont,SignedStudentsAmont = 0 ):


        self.NumCourse = int(NumCourse)
        self.NameCourse = NameCourse
        self.StudentAmount = int(SignedStudentsAmont)
        self.MaxStudents = int(MaxSignedStudentsAmont)
        self.FixMaxAndStudents()

    def __str__(self):
        return f"The Course name is {self.NameCourse} its id number is {self.NumCourse},its capacity is {self.MaxStudents} and there are currently {self.StudentAmount} signed to it "

    def GetPlacesLeft(self):
        return self.MaxStudents - self.StudentAmount

    def AddStudents(self, AddStudents) :
      if(AddStudents > 0) :
        if(self.GetPlacesLeft() > 0) :
            if(AddStudents >= self.GetPlacesLeft()) :
                AddStudents = AddStudents - self.GetPlacesLeft()
                self.StudentAmount = self.MaxStudents
                return AddStudents
            else :
                self.StudentAmount = self.StudentAmount + AddStudents
                AddStudents = 0
                return AddStudents
        else :
            print("The course has reached its maximum capacity")
            return AddStudents
      else :
          print("Please enter a correct amount of student to add")


    def FixMaxAndStudents(self):
        if(self.MaxStudents < self.StudentAmount) :
            self.StudentAmount = self.MaxStudents


