String = input("Please enter a string : ")
NewString = ""



for Char in String :
    if(Char not in NewString) :
        NewString = NewString + Char


"""for Char in String:
    if(NewString.count(Char) != 2) :
        NewString = NewString + Char + Char"""


print(NewString)

