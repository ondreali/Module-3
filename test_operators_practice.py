

import unittest

class OperatorsTest(unittest.TestCase):
    def test_equal(self):
        a = 17
        b = 8
        self.assertFalse(a==b)
    def test_notequal(self):
        a = 5
        b = 5
        self.assertFalse(a!=b)
    def test_greaterthan(self):
        a = 9
        b = 18
        self.assertFalse(a>b)
    def test_lessthan(self):
        a = 6
        b = 9
        self.assertTrue(a<b)
    def test_greaterthanorequalto(self):
        a = 10
        b = 9
        self.assertTrue(a>=b)
    def test_lessthanorequalto(self):
        a = 2
        b = 18
        self.assertTrue(a<=b)

if __name__ == '__main__':
    unittest.main()
