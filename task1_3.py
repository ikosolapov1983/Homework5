from task1_2 import Employee

class ITEmployee(Employee):

    def __init__(self, *args, **kwargs):     # создаем список параметров
        super().__init__(*args, **kwargs)
        self.skills = []

    def add_skill(self, new_skill):
        self.skills.append(new_skill)
        return self.skills

    def add_skills(self, new_skills):
        self.skills.extend(new_skills)
        return self.skills

    def __str__(self):
        return f"{self.full_name}, год рождения {self.year}, возраст {self.age_now}, должность {self.position} " \
                f" опыт работы {self.experience}, зарплата: {self.salary}, навыки: {self.skills}"

if __name__ == "__main__":
    p1 = ITEmployee("Vasya", "Petrov", 1974, "Driver", 7, 1000)
    print(p1.age_in())
    print(p1.full_name)
    print(p1.salary_add(500))
    print(p1.exp_position())
    print(p1.add_skill('cleaner'))
    print(p1.add_skills(['security guard', 'gardener']))
    print(p1)
