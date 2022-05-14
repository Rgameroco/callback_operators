import unittest

import practice

class TestPractice(unittest.TestCase):
    def test_1(self):
        self.assertEqual(practice.four(practice.times(practice.five())), 20)
    def test_2(self):
        self.assertEqual(practice.one(practice.plus(practice.eight())), 9)
    def test_3(self):
        self.assertEqual(practice.seven(practice.minus(practice.three())), 4)
    def test_4(self):
        self.assertEqual(practice.nine(practice.divided_by(practice.three())), 3)
    def test_5(self):
        self.assertEqual(practice.zero(practice.divided_by(practice.zero())), -1)
