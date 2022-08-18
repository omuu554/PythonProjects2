from Animal import Animal

Dog = Animal("Karla")
NumAction = int(input("Please enter an action (1 -3) to stop press (0): "))

while(NumAction != 0):

    if(NumAction == 1):
        Gram = int(input("Please enter the food amount in grams: "))
        Dog.eat(Gram)
        print(Dog.__str__())


    if (NumAction == 2):
        MinPlay = int(input("Please enter the amount of minutes to play: "))
        Dog.play(MinPlay)
        print(Dog.__str__())


    if (NumAction == 3):
        MinRest = int(input("Please enter the amount of minutes to rest: "))
        Dog.rest(MinRest)
        print(Dog.__str__())

    NumAction = int(input("Please enter an action (1 -3) to stop press (0): "))

print(Dog.__str__())