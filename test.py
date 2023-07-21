import unittest

from Calc import add, sub

class TestMathOp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)

    def test_sub(self):
        self.assertEqual(sub(4, 3), 1)
        self.assertEqual(sub(3, 4), -1)

if __name__ == '__main__':
    unittest.main()
