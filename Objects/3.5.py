NumAmount = int(input("How much numbers do you want to be created in fibunachis Series: "))
LastNum = 0
CurrentNum = 1
NextNum = LastNum + CurrentNum
if NumAmount <= 0 :
    print("Please enter a number bigger than 0")
else :

   for i in range(NumAmount) :
       if i <= 1 :
           print(f"{i},", end= '')
       else :
           if i != NumAmount -1:
              print(f"{NextNum}," , end= '')
           else :
               print(f"{NextNum}")
           LastNum = CurrentNum
           CurrentNum = NextNum

       NextNum =   LastNum +  CurrentNum

