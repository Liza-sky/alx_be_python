import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):


    def setUp(self):
        self.calc = SimpleCalculator()


    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)


    def test_substraction(self):
        self.assertEqual(self.calc.substraction(5, 3), 2)
        self.assertEqual(self.calc.substraction(3, 5), -2)
        self.assertEqual(self.calc.substraction(-5, -3), -2)
        self.assertEqual(self.calc.substraction(0, 0), 0)
        self.assertEqual(self.calc.substraction(2.5, 1.5), 1.0)


    def test_multiplication(self):
        self.assertEqual(self.calc.multiplication(4, 3), 12)
        self.assertEqual(self.calc.multiplication(-2, 5), -10)
        self.assertEqual(self.calc.multiplication(0, 100), 0)
        self.assertEqual(self.calc.multiplication(1.5, 2), 3.0)
        self.assertEqual(self.calc.multiplication(-1.5, -2), 3,0)


    def test_division(self):
        self.assertEqual(self.calc.division(10, 2), 5)
        self.assertEqual(self.calc.division(-6, 3), -2)
        self.assertEqual(self.calc.division(7.5, 2.5), 3.0)
        self.assertEqual(self.calc.division(10, 0))
        self.assertEqual(self.calc.division(0, 0))
        self.assertEqual(self.calc.division(0, 5), 0)

if __name__ == '__main__':
    unittest.main()