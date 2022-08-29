from random import randint

def Get_Amount(Num):
    while(not Num.isdigit()):
        Num = input("Please enter a correct amount of grades: ")

    return Num

def ListOfGrades(Num):
    ListOfG = []
    for GradeNum in range(int(Num)):
        Grade = randint(0,100)
        ListOfG.append(Grade)

    return ListOfG


#Number = input("Please enter an amount of grades: ")
#Number = Get_Amount(Number)
#print(ListOfGrades(Number))