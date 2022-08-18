
List = [0,1]
UserNum = int(input("Please enter a number: "))

for i in range(UserNum) :
    List.append(List[len(List) -1] + List[len(List) -2])


print(List)