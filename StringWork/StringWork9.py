String = input("Please enter a string : ")
String2 = input("Please enter a second string : ")
count = 0

for i in range(len(String)) :
    if(String[i].lower() in String2 or String[i].upper() in String2) :
        count += 1

print(count)