'''
Created on 28-Oct-2018

@author: vinee
'''
import math
class GeometricObjects:
    def __init__(self,color,filled):
        self.color=color
        self.filled=filled
    def getPerimeter(self):
        pass
    def getArea(self):
        pass
    
class Triangle(GeometricObjects):
    def __init__(self, color, filled, side1 = 1.0, side2 = 1.0, side3 = 1.0):
         GeometricObjects.__init__(self, color, filled) 
         self.side1 = side1 
         self.side2 = side2
         self.side3 = side3
        
    def getSide1(self):
        return self.side1
    def getSide2(self):
        return self.side2
    def getSide3(self):
        return self.side3
    def setSide2(self, side):
         self.side2 = side 
    def setSide3(self, side):
         self.side3 = side 
    def getPerimeter(self):
         return self.side1 + self.side2 + self.side3 
    def getArea(self): # Heron's
        p = self.getPerimeter() / 2; area = math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3)) 
        return area 
    def __str__(self): 
        return "Side 1 : " + str(self.side1) + "\n" + \
               "Side 2 : " + str(self.side2) + "\n" + \
               "Side 3 : " + str(self.side3) + "\n" + \
               "Perimeter : " + str(self.getPerimeter()) + "\n" + \
               "Area : " + str(self.getArea()) + "\n" + \
               "Filled : " + str(self.filled) + "\n" + \
               "Color : " + str(self.color)
 #test
triangle1 = Triangle("RED", True) 
triangle2 = Triangle("GREEN", False, 3, 4, 5) 
print("Triangle 1 : ")
print(triangle1) 
print("Triangle 2 : ") 
print(triangle2)
        