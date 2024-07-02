import unittest
from main import Calculator

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        output = Calculator('2+5 * 9 / 8')
        self.assertEqual(output.string, 7.625)
    
    def test_add_positive_numbers(self):
        output = Calculator('222 * 9871 - 13464 / 159753')
        self.assertEqual(output.string, 2191361.9157198924)

    

if __name__ == '__main__':
    unittest.main()