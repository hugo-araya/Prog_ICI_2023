import unittest
import kaprekar4gral

class TestKaprekar4gral(unittest.TestCase):

    def test_comprueba(self):
        self.assertEqual(kaprekar4gral.comprueba('1234'), True)
        self.assertEqual(kaprekar4gral.comprueba('1214'), True)
        self.assertEqual(kaprekar4gral.comprueba('1111'), False)
        
if __name__ == '__main__':
    unittest.main()