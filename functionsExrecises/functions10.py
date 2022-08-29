import sys
import os

global Grades

def InvalidGrade(Grade):
    while(Grade < 0 or Grade > 100):
            Grade = int(input("Please enter a grade correct: "))

    return Grade





def IsGradePassed(Grade):
    return Grade >= 70

def RestartScript():
    os.system("functions10.py")


for Grades in range(5):

   try:
    Grade = int(input("Please enter a grade: "))
    Grade = InvalidGrade(Grade)
    if (IsGradePassed(Grade)):
        print(f"The grade {Grade} has Passed")
    else:
        print(f"The grade {Grade} has Failed")
   except:
       break

if (Grades != 4):
    Grades = 0
    print("You have entered a Worse input Porgram Restarted")
    RestartScript()