import unittest
import calc

class TestCalc(unittest.TestCase):  
    
    def test_add(self):
        self.assertEqual((calc.add(9,4)), 13)
        self.assertEqual((calc.add(-1,-1)), -2)
        self.assertEqual((calc.add(8,1)), 9)
        self.assertEqual((calc.add(20,4)), 24)
        
    def test_multiply(self):
        self.assertEqual((calc.multiply(2,4)), 8)
        self.assertEqual((calc.multiply(-1,-1)), 1)
        self.assertEqual((calc.multiply(8,1)), 8)
        self.assertEqual((calc.multiply(20,4)), 80)
        
    def test_subtract(self):
        self.assertEqual((calc.subtract(9,4)), 5)
        self.assertEqual((calc.subtract(-1,-1)), 0)
        self.assertEqual((calc.subtract(8,1)), 7)
        self.assertEqual((calc.subtract(20,4)), 16)
        
    def test_division(self):
        self.assertEqual((calc.division(8,4)), 2)
        self.assertEqual((calc.division(-1,-1)), 1)
        self.assertEqual((calc.division(8,1)), 8)
        self.assertEqual((calc.division(20,4)), 5)
        
        with self.assertRaises(ValueError):
            calc.division(10,0)
    
        
if __name__ == '__main__':
    unittest.main()











