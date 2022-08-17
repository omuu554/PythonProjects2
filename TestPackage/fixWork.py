TestResult = int(input("Please enter a test result between(0 - 100): "))
TestCount = 0

while ( TestResult >= 0 and TestResult <= 100 ) :
    TestCount += 1

    if( TestCount ==5 ):
        print("Good job you have entered 5 test results!!!!!!")
        break

    TestResult = int(input("Please enter a test result between(0 - 100): "))
else:
 print("YOU HAVE ENTERED A BAD TEST RESULT!!!!")