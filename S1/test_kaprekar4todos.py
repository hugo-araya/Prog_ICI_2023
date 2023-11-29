import unittest
import kaprekar4todos

class TestKaprekar4todos(unittest.TestCase):
    
    def test_comprueba(self):
        self.assertEqual(kaprekar4todos.comprueba('5432'), True)
        self.assertEqual(kaprekar4todos.comprueba('5555'), False)        
        self.assertEqual(kaprekar4todos.comprueba('5453'), True)    
        self.assertEqual(kaprekar4todos.comprueba('5454'), True)  

if __name__ == '__main__':
    unittest.main()