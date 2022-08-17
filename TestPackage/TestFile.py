
def CHANGEX(x, y):
 x = x + 1
 if (x + y) > x :
    return x
 else :
    return y


x = int(input("Please enter a number: "))
y = int(input("Please enter a second number: "))
print(CHANGEX(x, y))
print(x)


print("Ignore")
x = "Hellow"
for y in x :
 print(ord(y))#תתעלמו מזה

#תרגיל 1
v = int(input("Please enter a number: "))
z = int(input("Please enter a second number: "))
print(f"{v} + {z} = {v+z}\n{v} - {z} = {v-z}\n{v} * {z} = {v*z}\n{v} / {z} = {v/z} ")





