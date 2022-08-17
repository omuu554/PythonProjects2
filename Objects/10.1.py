Num = input("Please enter number one: ")
Num2 = input("Please enter number two: ")
Num3 = input("Please enter number three: ")

def MaxNum(x, y, z) :
   if(x > y and x > z) :
       return x
   elif (y > x and y > z):
       return y
   else :
       return z

print(MaxNum(77,12,9))

