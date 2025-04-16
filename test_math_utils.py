import unittest
from math_utils import add, subtract

class TestMathUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 5), 10)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
