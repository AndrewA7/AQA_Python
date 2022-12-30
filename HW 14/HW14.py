from abc import abstractmethod


class Shape():
    @abstractmethod
    def draw(self):
        pass


class Triangle(Shape):
    def __init__(self, width: int):
        self.width = width

    def draw(self):
        str = 0
        for i in range(self.width):
            str += 1
            print("*" * str)
        return str


class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.height = height
        self.width = width

    def draw(self):
        for i in range(self.height):
            print("*" * self.width)
        return


figure_list = [Triangle(4), Rectangle(4, 6)]
for figure in figure_list:
    figure.draw()
    print("---------------------")
triangle = Triangle(4)
rectangle = Rectangle(4, 6)

