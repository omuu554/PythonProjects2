from Lottery import Lottery

L = Lottery("500")
L.Print()
Num = int(input("Please enter a number(1-45): "))
Guesses = 1
RightGuesses = 0



while( Num >= 1 and Num <= 45 ) :
      if( L.isNumInList(Num)):
          RightGuesses += 1

      if(Guesses == 6) :
          break
      Num = int(input("Please enter a number(1-45): "))
      Guesses += 1

if(Guesses != 6) :
    print("You have lost because of a bad number and you have won NOTHING!!!! ")
else :
    print(f"You got {RightGuesses} gusses right and have won {L.CorrectGuesses(RightGuesses)}")




L.Print()
