from newton_polynomial import polynomial
from numpy import array
from sympy import symbols
from unittest import main, TestCase


class TestStringMethods(TestCase):

    def test_1(self):
        x = array((1, 2, 3, 4, 5, 6, 7))
        y = array((52.5, 34, 13.5, 0, 2.5, 30, 91.5))
        p = polynomial(x, y)
        x_ = symbols('x')
        self.assertEqual(p, 1.5 * x_ ** 3 - 10.0 * x_ ** 2 + 1.0 * x_ + 60.0)

    def test_2(self):
        x = array([1, 2, 3, 4, 5, 6])
        y = array([0, 5, 22, 57, 116, 205])
        p = polynomial(x, y)
        x_ = symbols('x')
        self.assertEqual(p, 1.0 * x_ ** 3 - 2.0 * x_ + 1.0)


if __name__ == '__main__':
    main()
