ListString = []
count = 0


for i in range(5) :
    String = input("Please enter a string: ")
    ListString.append(String)

for i in ListString:
    if(len(i) >= 4 and i[0]==i[len(i)-1]) :
        count += 1

print(ListString)
print(count)