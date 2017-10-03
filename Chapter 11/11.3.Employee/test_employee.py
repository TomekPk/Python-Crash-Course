'''
Write a test case for Employee. Write two test methods, test_give_
default_raise() and test_give_custom_raise(). Use the setUp() method so
you don’t have to create a new employee instance in each test method. Run
your test case, and make sure both tests pass.
'''

import unittest
from employee import Employee


class EmployeeTestCase(unittest.TestCase):
    """Tests for employee.py"""

    def setUp(self):
        first_name = "David"
        last_name = "Moore"
        annual_salary = 10000
        self.new_employee = Employee(first_name, last_name,annual_salary)

    def test_give_default_raise(self):
        function = self.new_employee.give_raise()
        self.assertEqual(function, 15000)


    def test_give_custom_raise(self):
        function = self.new_employee.give_raise(raise_salary=123)
        self.assertEqual(function, 10123)

if __name__ == '__main__':
    unittest.main()
