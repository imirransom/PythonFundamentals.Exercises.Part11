class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2

class Square(Rectangle):
    def area(self):
        total = self.length * self.width
        return total * total

    def perimeter(self):
        total = (self.length + self.width) * 2
        return total * total

rect1 = Rectangle(2, 4)
print(rect1.area())
print(rect1.perimeter())

square1 = Square(8, 8)
print(square1.area())