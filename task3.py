import unittest
from task6_1 import treug, is_year_leap, triangle

class TestsTask6(unittest.TestCase):
    def testTreug(self):
        res = treug(5, 6, 8)
        self.assertEqual(res, True)

    def testTriangle(self):
        res = triangle(5, 5, 5)
        self.assertEqual(res, "Равносторонний треугольник")

    def testYear(self):
        res = is_year_leap(2000)
        self.assertEqual(res, True)

if __name__ == "__main__":
    unittest.main()
