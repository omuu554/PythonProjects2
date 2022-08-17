
#תרגיל 3
Number = input("Please enter a number with 3 Letters:")
if len(Number) == 3 :
    print(f"Is that your number: {Number[2]}{Number[1]}{Number[0]}")
    print(f"Is that your number: {int(Number)%10}{int(Number)//10%10}{int(Number)//100}")
else :
    print("Thats not your number")

