ListOfTestResults = []
AmountOfTests = int(input("Please enter the amount of test results: "))
NumPassed = 0
NumFailed = 0

while AmountOfTests != 0 :
    TestResult = int(input("Please enter a test result to be added to the list: "))
    if TestResult <= 100 and TestResult >= 1 :
        ListOfTestResults.append(TestResult)
        AmountOfTests -= 1
    else:
        print("Please enter a test result between 100 and 1 ")

for iTests in ListOfTestResults :
    if iTests >= 60 :
        NumPassed += 1
    else :
        NumFailed += 1

print(f"{NumPassed} tests have passed and, {NumFailed} test have Failed")