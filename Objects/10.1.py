Num1 = int(input("Please enter number one: "))
Num2 = int(input("Please enter number two: "))
Num3 = int(input("Please enter number three: "))

def MaxNum(x, y, z) :
   if(x > y and x > z) :
       return x
   elif (y > x and y > z):
       return y
   else :
       return z

print(MaxNum(Num1,Num2,Num3))

