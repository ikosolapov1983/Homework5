import math

class Point:

    def __init__(self, x=0, y=0):     # создаем список параметров
        self.point = [x, y]

    def zero_point(self):
        self.z = ((self.point[0] ** 2) + (self.point[1] ** 2)) ** 0.5
        return self.z

    def distance(self, x2, y2):
        point2 = [x2, y2]
        self.d = (((point2[0] - self.point[0]) ** 2) + ((point2[1] - self.point[1]) ** 2)) ** 0.5
        return self.d

    def system_k(self):                                               # цилиндрическая система
        self.p = math.sqrt((self.point[0] ** 2) + (self.point[1] ** 2))
        self.ph = math.atan2(self.point[1], self.point[0])
        return f'Радиус {self.p}, Угол {self.ph}'

    def __str__(self):
        return f"Расстояние до нулевой точки: {self.z}, расстояние между точками = {self.d}," \
               f" при переходе в цилиндрическую систему координат: радиус = {self.p}, угол = {self.ph}"

if __name__ == "__main__":
    p1 = Point(2.3, 4)
    print(p1.zero_point())
    print(p1.distance(8.5, 0.7))
    print(p1.system_k())
    print(p1)
