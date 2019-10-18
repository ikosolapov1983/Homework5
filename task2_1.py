class Rectangle:

    def __init__(self, a=0, b=0):     # создаем список параметров
        self.a = a
        self.b = b

    def area(self):
        self.c = self.a * self.b
        return self.c

    def perimeter(self):
        self.p = (self.a + self.b) * 2
        return self.p

    def __str__(self):
        return f"Стороны прямоугольника: a = {self.a}, b = {self.b}, площадь = {self.c}, периметр = {self.p}"


if __name__ == "__main__":
    p1 = Rectangle(18, 16)
    print(p1.area())
    print(p1.perimeter())
    print(p1)
