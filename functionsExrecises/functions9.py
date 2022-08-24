

def InvalidAge(Age):
    while(Age < 0 or Age > 120):
        Age = int(input("Please enter a correct age: "))

    return Age

def GetAgeGroup(Age):

    if(Age >= 0 and Age <= 18):
        return "Child"
    if(Age >= 19 and Age <= 60):
        return "Adult"

    return "Senior"


for Ages in range(5):
    Age = int(input("Please enter an age: "))
    Age = InvalidAge(Age)
    print(f"{Age} is an {GetAgeGroup(Age)}")