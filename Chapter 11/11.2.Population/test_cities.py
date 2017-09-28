'''
Write a second test called test_city_country_population() that verifies
you can call your function with the values 'santiago', 'chile', and
'population=5000000'. Run test_cities.py again, and make sure this new test
passes.
'''

import unittest
from city_functions import combine_city_and_country


class NameTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        """Do names like 'Warsaw, Poland' work?"""
        checking_names = combine_city_and_country("Warsaw", "Poland")
        self.assertEqual(checking_names, "Warsaw, Poland ")

    def test_city_country_population(self):
        checking_names = combine_city_and_country("Warsaw", "Poland", "population=2mln")
        self.assertEqual(checking_names, "Warsaw, Poland population=2mln")

if __name__ == '__main__':
    unittest.main()
