#תרגיל 5
Number1 = int(input("Please enter the first number: "))
Number2 = int(input("Please enter the second number: "))
Number3 = int(input("Please enter the third number: "))
NumConect = f"{Number1}{Number2}{Number3} "
if Number1 <= 9 and Number1 >= 1 and Number2 <= 9 and Number2 >= 1 and Number3 <= 9 and Number3 >= 1 :
    print(f"{NumConect} , {int(NumConect)*2}")
else :
    print("Please enter a right number!!!!!!")