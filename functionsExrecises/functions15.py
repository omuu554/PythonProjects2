from functions14 import Get_Amount,ListOfGrades

def GetAvrage(List):
    return sum(List)/len(List)

Number = input("Please enter an amount of grades: ")
Number = Get_Amount(Number)
ListGrades = ListOfGrades(Number)
print(GetAvrage(ListGrades), ListGrades)