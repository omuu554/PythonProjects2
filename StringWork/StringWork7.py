String = input("Please enter a string : ")
NewString = ""

for i in range(len(String)) :
    if(String[i] not in NewString) :
        NewString = NewString + String[i]


print(NewString)

