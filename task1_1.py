from datetime import datetime

class Person:

    def __init__(self, name="", surname="", year=0):     # создаем список параметров
        self.full_name = name + " " + surname
        self.year = year

    def name(self):
        return self.full_name.split()[0]

    def surname(self):
        return self.full_name.split()[1]

    def age_in(self, age=datetime.now().year):
        self.age_now = age - self.year
        return self.age_now

    def __str__(self):
        return f"{self.full_name}, год рождения {self.year}, возраст {self.age_now}"

if __name__ == "__main__":
    p1 = Person("Vasya", "Petrov", 1983)
    print(p1.age_in())
    print(p1.full_name)
    print(p1)
