DicTests = {}
NewDicTests = {}
KeyName = input("Please enter a student name: ")
TestResult = 0
#KeyUser = input("Please enter a guy who ows you money from the list: ")
ValueCount = 0

while(KeyName != "") :
   TestResult = int(input("Please enter test result: "))
   while(TestResult < 0 or TestResult > 100) :
       TestResult = int(input("Please enter a CORRECT test result(0 - 100): "))
   DicTests.update({KeyName: TestResult})
   KeyName = input("Please enter a student name: ")


for Keys in DicTests.keys() :
     if (DicTests[Keys] not in NewDicTests.values()) :
         NewDicTests = NewDicTests | {Keys: DicTests[Keys]}

DicTests = NewDicTests
print(DicTests)
