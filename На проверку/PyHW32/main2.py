import unittest
import module2

c = module2.Number()
c.number = 2


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = module2.Number()

    def testNum(self):
        self.assertEqual(self.calc.number, 0)
    def testNumSetter(self):
        self.calc.number=10
        self.assertEqual(self.calc.number, 10)

    def testBin(self):
        self.assertEqual(self.calc.bin(10), bin(10))

    def testOct(self):
        self.assertEqual(self.calc.oct(10), oct(10))

    def testHex(self):
        self.assertEqual(self.calc.hex(10), hex(10))

if __name__ == '__main__':
    unittest.main()