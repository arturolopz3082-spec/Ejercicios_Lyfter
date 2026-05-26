import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2


def main():
    circle1 = Circle(5)
    circle2 = Circle(10)
    print(circle1.get_area())
    print(circle2.get_area())

if __name__ == '__main__':
    main()