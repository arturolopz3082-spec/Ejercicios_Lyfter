from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radio = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radio

    def calculate_area(self):
        return math.pi * self.radio ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side + self.side + self.side + self.side

    def calculate_area(self):
        return self.side * self.side


class Rectangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.heigh = height
    def calculate_area(self):
        return self.base * self.heigh

    def calculate_perimeter(self):
        return 2 * (self.base + self.heigh)

def main():
    circle = Circle(10)
    print(f'área del circulo: {circle.calculate_area():.2f}')
    print(f'perímetro del circulo {circle.calculate_perimeter():.2f}')

    rectangle = Rectangle(10, 5)
    print(f'Perimetro del rectángulo {rectangle.calculate_perimeter():.2f}')
    print(f'Área del rectángulo {rectangle.calculate_area():.2f}')

    square = Square(10)
    print(f'Área del cuadrado: {square.calculate_area():.2f}')
    print(f'Perímetro del cuadrado: {square.calculate_perimeter():.2f}')

if __name__ == '__main__':
    main()