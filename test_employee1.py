import unittest
from employee import Employee
from unittest.mock import patch

class TestEmployee(unittest.TestCase):
    '''Employee test running'''
    @classmethod
    def setUpClass(cls):
        print("set up class")
        
    @classmethod
    def tearDownClass(cls):
        print("Tear Down class")

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Corey','Schafer',50000)
        self.emp_2 = Employee('Sue','Smith',100000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        '''Test for email'''
        print('test_email')

        self.assertEqual(self.emp_1.email, 'Corey.Schafer@gmail.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@gmail.com')
        
        self.emp_2.first = 'Solomon'
        self.emp_1.first = 'Angel'
        self.assertEqual(self.emp_1.email, 'Corey.Angel@gmail.com')
        self.assertEqual(self.emp_2.email, 'Sue.Solomon@gmail.com')
        
        
    def test_fullname(self):
        '''Test for full name'''
        print('test_fullname')
        
        self.assertEqual(self.emp_1.fullname, 'Schafer Corey')
        self.assertEqual(self.emp_2.fullname, 'Smith Sue')
        
        self.emp_2.first = 'Solomon'
        self.emp_1.first = 'Angel'
        self.assertEqual(self.emp_1.fullname, 'Angel Corey')
        self.assertEqual(self.emp_2.fullname, 'Solomon Sue')

    def test_apply_raise(self):
        ''' Test for apply raise'''
        print('test_apply_raise')

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()   
        
        self.assertEqual(self.emp_1.pay, 52000)
        self.assertEqual(self.emp_2.pay, 104000)
        
    def test_monthly_schedule(self):
        ''' Test for monthly schedule'''
        print("test monthly schedule")
        
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.txt = 'success'
            
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Corey/May')
            self.assertEqual(schedule, 'success')
        
            mocked_get.return_value.ok = False
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Corey/May')
            self.assertEqual(schedule, 'Opps!! Bad Response!')
            
if __name__ == '__main__':
    unittest.main()
