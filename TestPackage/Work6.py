TestResult = int(input("Please enter a test result: "))

if TestResult>= 0 and TestResult<=100 :
    if(TestResult>=70) :
        print("Test Passed")
    else :
        print("Test Failed")
else:
    print("Test result not allowed")