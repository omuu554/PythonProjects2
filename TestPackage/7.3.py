DicTests = {}
NewDicTests = {}
KeyName = input("Please enter a student name: ")
TestResult = int(input("Please enter test result: "))
#KeyUser = input("Please enter a guy who ows you money from the list: ")

while(KeyName != "") :
   if(TestResult >= 0 and TestResult <= 100) :
     DicTests.update({KeyName: TestResult})
   KeyName = input("Please enter a student name: ")
   if(KeyName != "") :
     TestResult = int(input("Please enter test result: "))

print(DicTests)

"""for Key, Value in DicTests.items() :
    if Value not in NewDicTests :
        NewDicTests[Value] = [Key]
    else :
        NewDicTests[Value].append(Key)"""

for Keys in DicTests.keys():
    if(DicTests[Keys] not in NewDicTests):
        NewDicTests[DicTests[Keys]] = Keys
    else :
        NewDicTests[DicTests[Keys]] += ","+ Keys

print(NewDicTests)
