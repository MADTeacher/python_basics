class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

class Square(Shape):
    def __init__(self, side=1, x=0, y=0):
        super().__init__(x, y)
        self.side = side

    def __str__(self):
        return super().__str__() + f', side: {self.side}'

class Circle(Shape):
    def __init__(self, radius=1, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return super().__str__() + f', side: {self.radius}'


if __name__ == "__main__":
    my_circle = Circle(x=10, y=5)
    my_square = Square(5, 25, 40)
    print(my_circle)
    print(my_square)
    my_square.move(35, 50)
    my_circle.move(10, 10)
    print(my_circle)
    print(my_square)
