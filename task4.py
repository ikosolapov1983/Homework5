import unittest
from task1_3 import ITEmployee

class TestsITEmployee(unittest.TestCase):

    def setUp(self):
        self.emp = ITEmployee("Ivan", "Petrov", 1974, "Driver", 7, 1000)

    def testFullName(self):
        self.assertEqual(self.emp.full_name, 'Ivan Petrov')

    def testYear(self):
        self.assertNotEqual(self.emp.year, 0)

    def testAge(self):
        self.assertNotEqual(self.emp.age_in, 0)

    def testNoPosition(self):
         self.assertIsNotNone(self.emp.position)

    def testExperience(self):
        self.assertIsNotNone(self.emp.experience)

    def testExpPosition(self):
        self.emp.experience = 6
        self.assertEqual(self.emp.exp_position(), f"Middle {self.emp.position}")

    def testNoSalary(self):
        self.assertIsNotNone(self.emp.salary)

    def testAddSalary(self):
        self.emp.salary_add(600)
        self.assertEqual(self.emp.salary, 1600)

    def testNoSkills(self):
        self.assertEqual(len(self.emp.skills), 0)

    def testAddSkill(self):
        self.emp.add_skill('Gardener')
        self.assertIn('Gardener', self.emp.skills)

    def testAddSkills(self):
        self.emp.add_skills(['cleaner', 'security guard'])
        self.assertEqual(['cleaner', 'security guard'], self.emp.skills)

if __name__ == "__main__":
    unittest.main()
