import unittest
import kaprekar

class TestKaprekar(unittest.TestCase):
    def test_may_men(self):
        self.assertEqual(kaprekar.may_men('4356'), '6543')

    def test_men_may(self):
        self.assertEqual(kaprekar.men_may('4356'), '3456')

    def test_diferencia(self):
        self.assertEqual(kaprekar.diferencia('5321', '5320'), '0001')

if __name__ == '__main__':
    unittest.main()