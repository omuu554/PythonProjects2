Num = int(input("Please enter a number: "))
count = True

if Num > 1 :
    for x in range(2 , Num) :
        if(Num % x == 0) :
            count = True
            break

    if(count > 0) :
        print("המספר לא ראשוני")
    else :
        print("המספר ראשוני")


elif Num < -1 :
    for x in range(-2 , Num) :
        if(Num % x == 0) :
            count = True
            break

    if (count > 0):
        print("המספר לא ראשוני")
    else:
        print("המספר ראשוני")

elif Num == 1 :
    print("המספר ראשוני")

elif Num == 0 :
    print("המספר לא ראשוני")