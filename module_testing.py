import unittest
from solution import Positions, Programmer


class TestProgrammer(unittest.TestCase):

    def test_init(self):

        programmer = Programmer("Alexey", Positions.JUNIOR)
        self.assertEqual(programmer._Programmer__name, "Alexey")
        self.assertEqual(programmer._Programmer__position, Positions.JUNIOR)
        self.assertEqual(programmer._Programmer__hour_price, Positions.JUNIOR.value)

    def test_work(self):
        programmer = Programmer("Alexey", Positions.JUNIOR)
        programmer.work(150)
        self.assertEqual(programmer._Programmer__times, 150)

    def test_rise(self):
        programmer = Programmer("Alexey", Positions.JUNIOR)
        programmer.rise()
        self.assertEqual(programmer._Programmer__position, Positions.MIDDLE)
        self.assertEqual(programmer._Programmer__hour_price, Positions.MIDDLE.value)

        programmer.rise()
        self.assertEqual(programmer._Programmer__position, Positions.SENIOR)
        self.assertEqual(programmer._Programmer__hour_price, Positions.SENIOR.value)

        programmer.rise()
        self.assertEqual(programmer._Programmer__hour_price, Positions.SENIOR.value + 2)

    def test_info(self):
        programmer = Programmer("Alexey", Positions.JUNIOR)
        programmer.work(150)
        self.assertEqual(programmer.info(), "Alexey: 150 ч. 1500 тгр.")


if __name__ == '__main__':
    unittest.main()
