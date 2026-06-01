from abc import ABC, abstractmethod
from math import hypot
class Shape(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @property
    def is_large(self):
        return self.area() > 100
    

class Triangle(Shape):
    def __init__(self, leg_a, leg_b):
        super().__init__()
        self.leg_a = leg_a
        self.leg_b = leg_b
        
    def area(self):
        area_t = (self.leg_a * self.leg_b)/2
        return area_t
    
    def perimeter(self):
        hypotenuse = hypot(self.leg_a,self.leg_b)
        return hypotenuse + self.leg_a +self.leg_b
    
    
class Rectangle(Shape):
    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return 2*(self.width + self.length)
    
class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self):
        return self.side **2
    
    def perimeter(self):
        return self.side *4
    
if __name__ == "__main__":
     shapes = [
        Triangle(3, 4),
        Rectangle(5, 10),
        Square(20),
    ]
    
for shape in shapes:
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
    print(f"Large: {shape.is_large}")
    print()