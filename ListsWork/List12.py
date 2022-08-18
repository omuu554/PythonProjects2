List = []
String = input("Please give a string: ")

for i in range(len(String)) :
    if(String[i] not in List) :
        List.append(String[i])

print(List)


