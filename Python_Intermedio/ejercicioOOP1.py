import math

class Circle:
    #se crea un circulo con radio uno para que exista
    radius = 1

    def get_area(self):
        if self.radius > 0:
            return math.pi * (self.radius ** 2)
        else:
            print("El valor es negativo")

def main():
    circle = Circle()
    circle.radius = 2.5
    print(circle.get_area())

main()