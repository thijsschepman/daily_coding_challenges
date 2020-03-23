import unittest

from daily_challenge_5 import car, cdr, cons


class MyTestCase(unittest.TestCase):
    def test_car_returns_first_element_of_pair(self):
        self.assertEqual(3, car(cons(3, 4)))
        self.assertEqual(4, car(cons(4, 5)))

    def test_cdr_returns_last_element_of_pair(self):
        self.assertEqual(4, cdr(cons(3, 4)))
        self.assertEqual(5, cdr(cons(4, 5)))


if __name__ == '__main__':
    unittest.main()
