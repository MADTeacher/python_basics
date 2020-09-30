import unittest
from src.calculation import Calculation

class TestCalculation(unittest.TestCase):

    def setUp(self) -> None:
        #Метод запускается перед каждым тестом
        self.calculator = Calculation()

    def tearDown(self) -> None:
        #Метод запускается после каждого тестом
        ...

    def test_sum(self):
        self.assertEqual(self.calculator.sum(5, 3), 8)

    def test_sub(self):
        self.assertEqual(self.calculator.sub(10, 3), 6)

    def test_div(self):
        self.assertEqual(self.calculator.div(10, 3), 3)

    def test_mul(self):
        self.assertEqual(self.calculator.mul(5, 3), 14)

    def test_pow(self):
        self.assertEqual(self.calculator.pow2(5), 25)


if __name__ == "main":
    unittest.main()