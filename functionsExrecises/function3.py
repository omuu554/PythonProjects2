def PrintInNum(String, Num):
    for Times in range(Num):
        print(String)


Name = input("Please enter a name: ")
Number = int(input("Please enter the amount of times the name will print: "))

PrintInNum(Name,Number)