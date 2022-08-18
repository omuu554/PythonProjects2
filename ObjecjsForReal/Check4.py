

class Circle:


    def __init__(self,Radius):
        self.r = abs(int(Radius))
        self.PI = 3.14


    def area(self):
        return self.PI *pow(self.r, 2)

    def circumference(self):
        return 2*self.r*self.PI

