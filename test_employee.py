import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    '''Employee test running'''
    def test_email(self):
        '''Test for email'''
        emp_1 = Employee('Corey','Schafer',50000)
        emp_2 = Employee('Sue','Smith',50000)
        self.assertEqual(emp_1.email, 'Corey.Schafer@gmail.com')
        self.assertEqual(emp_2.email, 'Sue.Smith@gmail.com')
        
        emp_2.first = 'Solomon'
        emp_1.first = 'Angel'
        self.assertEqual(emp_1.email, 'Corey.Angel@gmail.com')
        self.assertEqual(emp_2.email, 'Sue.Solomon@gmail.com')
        
        
    def test_fullname(self):
        '''Test for full name'''
        emp_1 = Employee('Corey','Schafer',50000)
        emp_2 = Employee('Sue','Smith',50000)
        self.assertEqual(emp_1.fullname, 'Schafer Corey')
        self.assertEqual(emp_2.fullname, 'Smith Sue')
        
        emp_2.first = 'Solomon'
        emp_1.first = 'Angel'
        self.assertEqual(emp_1.fullname, 'Angel Corey')
        self.assertEqual(emp_2.fullname, 'Solomon Sue')
        
    def test_apply_raise(self):
        ''' Test for apply raise'''
        emp_1 = Employee('Corey','Schafer',50000)
        emp_2 = Employee('Sue','Smith',100000)
        
        emp_1.apply_raise()
        emp_2.apply_raise()   
        
        self.assertEqual(emp_1.pay, 52000)
        self.assertEqual(emp_2.pay, 104000)
        
if __name__ == '__main__':
    unittest.main()
        