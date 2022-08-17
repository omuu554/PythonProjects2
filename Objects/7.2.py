Dic = {}
Key = input("Please enter a guy who ows you money: ")
Num = int(input("Please enter how much money does any one cost: "))
KeyUser = input("Please enter a guy who ows you money from the list: ")

while(Key != "") :
    Dic.update({Key: Num})
    Key = input("Please enter a guy who ows you money: ")
    if(Key != "") :
     Num = int(input("Please enter how much money does any one cost: "))

if KeyUser in Dic :
    print("Found the bastard")
    Dic.pop(KeyUser)
else :
    print("Well get him next time boys")
