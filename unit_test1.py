#!/usr/bin/python3
import unittest
import math
from calculator import trig_calculator


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = trig_calculator()

    def test_case1(self):
        self.assertEqual(self.calculator.tan(math.radians(45),1))

    def test_case2(self):
        self.assertEqual(self.calculator.sin(math.radians(0),0))

    def test_case3(self):
        self.assertEqual(self.calculator.cos(math.radians(60),0.5))


if __name__ == '__main__':
    unittest.main()