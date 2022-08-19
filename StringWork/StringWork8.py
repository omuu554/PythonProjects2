String = input("Please enter a string : ")
List = []

for i in range(len(String)) :
    if(String.count(String[i]) > 1 and String[i] not in List) :
        print(f"The char {String[i]} is shown : {String.count(String[i])} in the word {String}")
        List.append(String[i])
