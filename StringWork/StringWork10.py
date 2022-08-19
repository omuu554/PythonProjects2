import random

String = input("Please enter a string : ")
Password = ""
List = []


for i in range(len(String)) :
    List.append(String[i])

for i in range(6) :
    Char = random.choice(List)
    Password = Password + Char

print(Password)
