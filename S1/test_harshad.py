import unittest
import harshad

class TestHarshad(unittest.TestCase):
    def test_suma_digitos(self):
        self.assertEqual(harshad.suma_digitos(162), 9)
        self.assertEqual(harshad.suma_digitos(111), 3)
        self.assertEqual(harshad.suma_digitos(123), 6)

if __name__ == '__main__':
    unittest.main()