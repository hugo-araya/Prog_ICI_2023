import unittest
import calcula

class TestCalcula(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(calcula.suma(20,10), 30)
    
    def test_resta(self):
        self.assertEqual(calcula.resta(20,10), 10)

    def test_multi(self):
        self.assertEqual(calcula.resta(20,10), 10)

    def test_divide(self):
        self.assertEqual(calcula.resta(20,10), 10)

if __name__ == '__main__':
    unittest.main()

