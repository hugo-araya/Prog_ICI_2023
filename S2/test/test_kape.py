import unittest
import kape 

class TestKape(unittest.TestCase):
    def test_may_men(self):
        self.assertEqual(kape.may_men('3524'), '5432')

    def test_men_may(self):
        self.assertEqual(kape.men_may('3524'), '2345')

if __name__ == '__main__':
    unittest.main()