String = input("Please enter a string : ")

String = String[0].upper() + String[1:]
#if(String[0].islower()):
 #String = String.replace(String[0],chr(ord(String[0])-32))

print(String)

