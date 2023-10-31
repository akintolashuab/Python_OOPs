import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    '''Employee test running'''
    
    def setUp(self):
        self.emp_1 = Employee('Corey','Schafer',50000)
        self.emp_2 = Employee('Sue','Smith',100000)
    
    def tearDown(self):
        pass
        
    def test_email(self):
        '''Test for email'''
        
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@gmail.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@gmail.com')
        
        self.emp_2.first = 'Solomon'
        self.emp_1.first = 'Angel'
        self.assertEqual(self.emp_1.email, 'Corey.Angel@gmail.com')
        self.assertEqual(self.emp_2.email, 'Sue.Solomon@gmail.com')
        
        
    def test_fullname(self):
        '''Test for full name'''
        
        self.assertEqual(self.emp_1.fullname, 'Schafer Corey')
        self.assertEqual(self.emp_2.fullname, 'Smith Sue')
        
        self.emp_2.first = 'Solomon'
        self.emp_1.first = 'Angel'
        self.assertEqual(self.emp_1.fullname, 'Angel Corey')
        self.assertEqual(self.emp_2.fullname, 'Solomon Sue')
        
    def test_apply_raise(self):
        ''' Test for apply raise'''
       
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()   
        
        self.assertEqual(self.emp_1.pay, 52000)
        self.assertEqual(self.emp_2.pay, 104000)
        
if __name__ == '__main__':
    unittest.main()
        