from task1_1 import Person

class Employee(Person):

    def __init__(self, name='', surname='', year=0, position="", experience=0, salary=0):     # создаем список параметров
        super().__init__(name, surname, year)
        self.position = position
        self.experience = experience
        self.salary = salary

    def exp_position(self):
        if self.experience > 6:
            return f"Senior {self.position}"
        if 3 < self.experience <= 6:
            return f"Middle {self.position}"
        else:
            return f"Junior {self.position}"

    def salary_add(self, increase):
        self.salary = self.salary + increase
        return self.salary


    def __str__(self):
        return f"{self.full_name}, год рождения {self.year}, возраст {self.age_now}, " \
               f"должность {self.position} опыт работы {self.experience}, зарплата: {self.salary}"

if __name__ == "__main__":
    p1 = Employee("Vasya", "Petrov", 1974, "Driver", 7, 1000)
    print(p1.age_in())
    print(p1.full_name)
    print(p1.salary_add(500))
    print(p1.exp_position())
    print(p1)
