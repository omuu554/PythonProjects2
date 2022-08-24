

def PrintNumbersBetween(Num1, Num2):
    for Numbers in range(min(Num1,Num2), max(Num1,Num2) + 1):
        print(Numbers, end= " ")


Number1 = int(input("Please enter a number: "))
Number2 = int(input("Please enter a second number: "))
PrintNumbersBetween(Number1,Number2)