from Bus import Bus


B = Bus(30)
UserAction = int(input(f"Please Choose an action\n(1)Passanger on\n(2)Passanger off\n(0)Stop actions\nChoose: "))

while(UserAction != 0 ):
    if(UserAction == 1) :
        PassangerName = input("Please enter a passangers name: ")
        B.getOn(PassangerName)
    elif (UserAction == 2) :
        PassangerName = input("Please enter a passangers name: ")
        B.getOff(PassangerName)

    UserAction = int(input(f"Please Choose an action\n(1)Passanger on\n(2)Passanger off\n(0)Stop actions\nChoose: "))


print(B.__str__())
