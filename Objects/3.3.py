import random

Num = random.randrange(1,10)
UserNum = int(input("Please guesss the number: "))

while Num != UserNum :
   if UserNum > 9 or UserNum < 1 :
       print("Please enter a number Between and including 9 and 1 ")
   else :
       if Num > UserNum:
           print("The Number is bigger than the number you chose.")
       elif Num < UserNum:
           print("The Number is smaller than the number you chose.")

   UserNum = int(input("Please guesss the number again: "))

print("YOU FOUND THE NUMBER!!!!!")