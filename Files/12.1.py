

x = open("Story.txt", 'w')
x.write("A boy is playing there.\nThere is a playground.\nAn airplane is in the sky.\nThe sky is pink\nAlphabet and numbers are allowed in the password")
x.close()

with open("Story.txt",'r+') as S:
    print(S.readlines())