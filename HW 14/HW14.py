from abc import abstractmethod


class Shape():
    @abstractmethod
    def draw(self):
        pass


class Triangle(Shape):
    def __init__(self, width: int):
        self.width = width

    def draw(self, width):
        str = 0
        for i in range(width):
            str += 1
            print("*" * str)
        return str


class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.height = height
        self.width = width

    def draw(self, width, height):
        for i in range(height):
            print("*" * width)
        return


triangle = Triangle
rectangle = Rectangle

triangle.draw(Triangle, 4)
print("---------------------")
rectangle.draw(Rectangle, 4, 6)
