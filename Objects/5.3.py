import re

Address = input("Please enter the city, street, number of house(Thats the format): ")
ListAddress = []

if  ' ,' in Address :
    ListAddress = Address.split(' ,')
elif  ', ' in Address :
    ListAddress = Address.split(', ')
elif ',' in Address :
    ListAddress = Address.split(',')

print(f"{ListAddress[0]}\n{ListAddress[1]}\n{ListAddress[2]}")

ListAdress = re.split(', | ,| |,',  Address)
print(f"{ListAdress[0]}\n{ListAdress[1]}\n{ListAdress[2]}")