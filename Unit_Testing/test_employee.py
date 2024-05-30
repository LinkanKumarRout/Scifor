import unittest
from employee import Employee
from unittest.mock import patch

# in this case when we use setUp and tearDown, order of exection of testcases are not fixed
# setUpClass is executed before all execution started.
# tearDownClass is executed after all execution is completed.
class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')
    
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    # this function runs before each test case
    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafor', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        print('tearDown\n')
    
    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Corey.Schafor@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafor@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')
    
    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Corey Schafor')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafor')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
    
    # this is used for mocking. this is not often used
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafor/May')

            self.assertEqual(schedule, "Success")

if __name__ == '__main__':
    unittest.main()