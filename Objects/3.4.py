import random

MaxRange = 101
MinRange = 1
UserNum = int(input("Please enter a number: "))
ComputerNum = random.randrange(MinRange , MaxRange)
ComputerGuess = 1


if UserNum > 100 or UserNum < 0 :
    print("The Number you entered HAS to be between and including 100 and 0")
else :
    while UserNum != ComputerNum :
        print(f"Computer number is {ComputerNum}")
        if ComputerNum < UserNum :
            print("Computer the number is bigger")
            MinRange = ComputerNum + 1

        elif ComputerNum > UserNum:
            print("Computer the number is smaller")
            MaxRange = ComputerNum

        ComputerNum = random.randrange(MinRange , MaxRange)
        ComputerGuess += 1

    print(f"Computer you got it the number is {UserNum} and it only took you {ComputerGuess} times")