
def CheckIfPowMinus(Num2):
    return Num2 < 0

def GetPow(Num1,Num2):
   Pow = 1
   if(not CheckIfPowMinus(Num2)):
     for i in range(Num2):
         Pow *= Num1

   else:
       for i in range(abs(Num2)):
           Pow *= 1/Num1

   return Pow


Number1 = int(input("Please enter a number: "))
Number2 = int(input("Please enter a second number: "))
print(GetPow(Number1, Number2))
