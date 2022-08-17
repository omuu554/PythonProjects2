Age = int(input("Please enter an age: "))

if Age>= 0 and Age<= 18 :
    print("Child")
elif Age>= 19 and Age<=60 :
    print("adult")
elif Age>= 61 and Age<= 120 :
    print("Senior")
elif Age>121 :
    print("World Record")
else:
    print("NotBorn")