import unittest
import kaprekar

class TestKaprekar(unittest.TestCase):
    def test_may_men(self):
        self.assertEqual(kaprekar.may_men('3245'), '5432')

    def test_men_may(self):
        self.assertEqual(kaprekar.men_may('3245'), '2345')
    
    def test_diferencia(self):
        self.assertEqual(kaprekar.diferencia('5432', '5431'), '0001')

if __name__ == '__main__':
    unittest.main()