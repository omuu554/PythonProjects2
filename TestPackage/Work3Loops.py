Num1 = int(input("Please enter an even number: "))
Num2 = int(input("Please enter an even number: "))

while(Num1 % 2 == 0 and Num2 % 2 == 0) :
    print(f"The sum of the 2 Even Numbers is : {Num1 + Num2}")

    Num1 = int(input("Please enter an even number: "))
    Num2 = int(input("Please enter an even number: "))

print(f"You have entered an odd number so you got: {Num1 * Num2}")