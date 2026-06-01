from abc import ABC, abstractmethod
from math import hypot
class Shape(ABC):
    """The shared parent for every shape. It requires each shape to define its own
    area and perimeter, and adds a check for whether the shape counts as large."""
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        """Returns the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Returns the perimeter of the shape."""
        pass

    @property
    def is_large(self):
        """Tells you whether the shape's area is greater than 100."""
        return self.area() > 100
    

class Triangle(Shape):
    """A right triangle defined by its two legs, which double as its base and height."""
    def __init__(self, leg_a, leg_b):
        super().__init__()
        self.leg_a = leg_a
        self.leg_b = leg_b
        
    def area(self):
        """Returns the area by treating the two legs as base and height."""
        area_t = (self.leg_a * self.leg_b)/2
        return area_t
    
    def perimeter(self):
        """Works out the hypotenuse from the two legs, then adds all three sides together."""
        hypotenuse = hypot(self.leg_a,self.leg_b)
        return hypotenuse + self.leg_a +self.leg_b
    
    
class Rectangle(Shape):
    """A rectangle defined by its width and length."""
    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length

    def area(self):
        """Returns the area by multiplying width and length."""
        return self.width * self.length
    
    def perimeter(self):
        """Returns the perimeter by adding the sides and doubling the total."""
        return 2*(self.width + self.length)
    
class Square(Shape):
    """A square defined by the length of one side."""
    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self):
        """Returns the area by squaring the side."""
        return self.side **2
    
    def perimeter(self):
        """Returns the perimeter by multiplying the side by four."""
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