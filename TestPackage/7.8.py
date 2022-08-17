import re

DicTestResults = {}
NameList = []
ResultsList = []
AboveAvrageNames = []

NameCount = 5
TestCount = 0
SumOfValues = 0
AvrageValues = 0

while (NameCount != 0) : # Creates a names list
    NameInput = input("Please enter a name for a student: ")

    if(NameInput == "" or re.search('\d', NameInput) or not NameInput.isalpha()) or NameInput in NameList :
        print("Please enter a CORRECT name!!!!!!")
    else :
        NameList.append(NameInput)
        NameCount -= 1

while (TestCount != 5) : #Creates a test list
    TestInput = input(f"Please enter a test result for the student {NameList[TestCount]}: ")

    if(TestInput == "" or not TestInput.isdigit() or int(TestInput) >= 0 and int(TestInput) >= 100) :
        print("Please enter a CORRECT test result!!!!!!")
    else :
         ResultsList.append(int(TestInput))
         TestCount += 1

for Merge in range(5) : # Megres the 2 lists
    DicTestResults.update({NameList[Merge] : ResultsList[Merge]})
    SumOfValues = SumOfValues +  ResultsList[Merge] # Calculates the sum of the results

AvrageValues = SumOfValues / 5 # Calculates the avrage of the results

for keys in DicTestResults.keys() : # creates a list of the names with the biggest avrage
    if(DicTestResults[keys] > AvrageValues) :
        AboveAvrageNames.append(keys)

print(f"The students : {', '.join(map(str,AboveAvrageNames))}. have a test result above the avrage {AvrageValues}")

