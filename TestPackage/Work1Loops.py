Num = int(input("Please enter a number bigger than 99 and smaller than 1000: "))

while(Num >= 100 and Num <=999) :
    print(f"The sum is {Num%10 + Num//10%10 + Num//100}")

    Num = int(input("Please enter a number bigger than 99 and smaller than 1000(diffrente to stop): "))

print("Error")