import unittest
import calcula

class TestCalcula(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(calcula.suma(10, 5), 15)
        self.assertEqual(calcula.suma(10, 5), 15)

    def test_resta(self):
        self.assertEqual(calcula.resta(100,9), 91)

    def test_multi(self):
        self.assertEqual(calcula.multi(10, 5), 50)

    def test_divide(self):
        self.assertEqual(calcula.divide(10, 5), 2)

if __name__ == '__main__':
    unittest.main()
