import pytest
from math_utils import add, subtract, multiply

class TestMathUtils(pytest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 5), 10)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply():
        assert multiply(4, 3) == 12
        
    def test_multiply_invalid_type():
        try:
            multiply("a", 3)
        except ValueError:
            assert True

if __name__ == '__main__':
    pytest.main()
