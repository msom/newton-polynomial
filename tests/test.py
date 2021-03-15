from newton_polynomial import coefficients, polynomial
from numpy import array
from sympy import symbols
from unittest import main, TestCase


class TestStringMethods(TestCase):

    def test_polynomial(self):
        x = array((1, 2, 3, 4, 5, 6, 7))
        y = array((52.5, 34, 13.5, 0, 2.5, 30, 91.5))
        a = coefficients(x, y)

        self.assertListEqual(list(a), [52.5, -18.5, -1., 1.5, 0., 0., 0.])

        p = polynomial(a, x)

        x_ = symbols('x')
        self.assertEqual(p, 1.5 * x_ ** 3 - 10.0 * x_ ** 2 + 1.0 * x_ + 60.0)


if __name__ == '__main__':
    main()
