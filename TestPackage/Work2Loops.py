Age = int(input("Please enter an age between 0-120: "))

while(Age>= 0 and Age<=120) :
    if(Age>= 0 and Age<=18) :
        print("Child")
    elif (Age >= 19 and Age <= 60) :
        print("adult")
    else :
        print("senior")

    Age = int(input("Please enter an age between 0-120: "))

print("Age is not between 0-120 ")