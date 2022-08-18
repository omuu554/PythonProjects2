from Work3 import Person

P = Person("Josh1",-1,-1)

P.Show()

if(P.HasChildren()): print("Has Children")
else: print("No Children")

print(f"{P.Name} is a {P.AgeGroup()}")
