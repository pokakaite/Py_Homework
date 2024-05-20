import unittest
import module1

class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = module1.NumbersCalculator()

    def testSumm(self):
        self.assertEqual(self.calc.summ(1,2,3), 6)

    def testAverage(self):
        self.assertEqual(self.calc.average(1, 2, 3), 2)

    def testMax(self):
        self.assertEqual(self.calc.max(1, 2, 3), 3)

    def testMin(self):
        self.assertEqual(self.calc.min(1, 2, 3), 1)


if __name__ == '__main__':
    unittest.main()