'''
Created on 30-Oct-2018

@author: vinee
'''
import math
import sys

class TriangleError(RuntimeError):
    def __init__(self,s1,s2,s3):
        self.side1=s1
        self.side2=s2
        self.side3=s3
    def getS1(self):
        return self.side1 
    def getS2(self):
        return self.side2
    def getS3(self):
        return self.side3
    def printError(self):
        print("The sum of any two sides should be greater than third side")
        sys.exit()  
        
class GeometricObject:
    def __init__(self,color,filled):
        self.color=color
        self.filled=bool(filled)
    def getColor(self):
        return self.color
    def getFilled(self):
        return self.filled
    
class Triangle(GeometricObject):
    def __init__(self,color,filled,s1,s2,s3):
        GeometricObject.__init__(self, color, filled)
        self.side1=s1;
        self.side2=s2
        self.side3=s3
        try:
            if self.side1+self.side2<=self.side3 or self.side1+self.side3<=self.side2 or self.side2+self.side3<=self.side1:
                raise TriangleError(self.side1,self.side2,self.side3)
            else:
                pass
        except TriangleError as e:
            e.printError()
    def getSide1(self):
        return self.side1
    def getSide2(self):
        return self.side2
    def getPerimeter(self):
        return self.side1+self.side2+self.side3
def main():
    s1=int(input("Enter side1:"))
    s2=int(input("Enter side2:"))
    s3=int(input("Enter side3:"))
    c=input("Enter color")
    f=int(input("Enter if filled or not:"))
    t1=Triangle(c,f,s1,s2,s3)
    
    print("Perimeter",t1.getPerimeter())
main()
           