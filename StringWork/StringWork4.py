String = input("Please enter a string : ")
Count = 0


while(String != "") :
    String = String[1:]
    Count += 1

print(Count)

