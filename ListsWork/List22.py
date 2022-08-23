import random

digits = ""
UserNum = input("Please enter a number: ")
hits = 0
boolCount = 0

for i in range(4):

    digit = random.randint(0,9)
    while(str(digit) in digits):
        digit = random.randint(0, 9)

    digits += str(digit)

print(digits)

while(UserNum != digits):
    for i in range(len(UserNum)):
        if(UserNum[i] == digits[i]):
            boolCount += 1
        if(UserNum[i] != digits[i] and UserNum[i] in digits):
            hits += 1


    print(f"bools: {boolCount}, hits: {hits}")
    UserNum = input("Please enter a number: ")
    hits = 0
    boolCount = 0







