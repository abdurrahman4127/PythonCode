class Shape:
    def __init__(self, name):
        self.name = name

    def print_shape(self):
        print(self.name)

    
class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)    # class Shape expects one argument

        self.length = length
        self.width = width
    
    def print_rectangle(self):
        area = self.length * self.width
        print(f"area of the rectangle: {area}")


class Triangle(Rectangle):
    def __init__(self, name, base, height):
        super().__init__(name, base, height)   # class Rectangle expects 2 argument

        self.base = base
        self.height = height
    
    def print_triangle(self):
        area = 0.5 * self.base * self.height
        print(f"triangle's area: {area}")


ob1 = Shape("it needs to be pointy")  # qoute by Aladeen
ob1.print_shape()

ob2 = Rectangle("", 10, 70)    # super().__init__(self, name, length, width)
ob2.print_rectangle()

ob2 = Triangle("", 7, 10)      # super().__init__(self, name, base, height)
ob2.print_triangle()