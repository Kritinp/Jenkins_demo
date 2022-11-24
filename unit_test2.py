#!/usr/bin/python3
import unittest
import math
from calculator import trig_calculator


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = trig_calculator()

    def test_case1(self):
        self.assertEqual(self.calculator.tan(math.radians(45)),3.2)

    def test_case2(self):
        self.assertEqual(self.calculator.sin(math.radians(45)),3.2)

    def test_case3(self):
        self.assertEqual(self.calculator.cos(math.radians(45)),3.2)
        


if __name__ == '__main__':
    unittest.main()