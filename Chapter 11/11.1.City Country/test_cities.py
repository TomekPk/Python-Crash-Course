'''

Create a file called test_cities.py that tests the function you just wrote
(remember that you need to import unittest and the function you want to test).
Write a method called test_city_country() to verify that calling your function
with values such as 'santiago' and 'chile' results in the correct string. Run
test_cities.py, and make sure test_city_country() passes.
'''

import unittest
from city_functions import combine_city_and_country


class NameTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        """Do names like 'Warsaw, Poland' work?"""
        checking_names = combine_city_and_country("Warsaw", "Poland")
        self.assertEqual(checking_names, 'Warsaw, Poland')


if __name__ == '__main__':
    unittest.main()
