class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2

class Square(Rectangle):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length

    def perimeter(self):
        return self.length * 4

rect1 = Rectangle(2, 4)
print(rect1.area())
print(rect1.perimeter())

square1 = Square(8)
print(square1.area())
print(square1.perimeter())