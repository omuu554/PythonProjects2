

class HardDisk:
    def __init__(self,NumItems, SpaceTakeGB):
        self.ItemAmount = int(NumItems)
        self.GBFull = int(SpaceTakeGB)
        self.MaxGB = 100
        self.__FixGB()
        self.__FixItems()

    def __FixGB(self):
        if(self.MaxGB < self.GBFull) :
             self.__SetGB(self.MaxGB)
        if(self.GBFull <= 0) :
             self.__SetGB(0)
             self.__SetItems(0)

    def __FixItems(self):
        if(self.GBFull == 0):
            self.__SetItems(0)
        if(self.ItemAmount < 0) :
            self.__SetItems(0)
            self.__SetGB(0)
        if (self.ItemAmount == 0):
            self.__SetGB(0)



    def __SetGB(self, GB):
        self.GBFull = GB

    def __SetItems(self,Items):
        self.ItemAmount = Items


    def Show(self):
        print(f"The Disk Has {self.MaxGB} GB of space,it holds {self.ItemAmount} items that are taking {self.GBFull} of GB")

    def freeSpace(self):
        return self.MaxGB - self.GBFull

    def addFile(self,FileSize):
        if(FileSize + self.GBFull <= self.MaxGB) :
           GBFull = FileSize + self.GBFull
           self.__SetGB( GBFull)
           self.__SetItems(self.ItemAmount+1)
           return "Succsses"
        else :
           return "Failure"

    def delFile(self,FileSize):
        if (self.GBFull - FileSize < 0):
            self.__SetGB(0)
            self.__SetItems(0)
        else :
            GBFull = self.GBFull - FileSize
            self.__SetGB(GBFull)
            self.__SetItems(self.ItemAmount - 1)

