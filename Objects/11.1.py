INPUT = input("Just Choose Something: ")
class Error() :
    def __init__(self,Health):
        self.Health = int(Health)

    def main(self,Health):
       try :
           self.Health = int(Health)
       except:
           raise Exception("Please enter a number")
       finally:
           print("End Of Porgram")


boss = Error("12")
boss.main(INPUT)


