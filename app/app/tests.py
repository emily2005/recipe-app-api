"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    """Test calc module"""

    def test_add_numbers(self):
        """Test adding numers together by running thru the calc add function"""

        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_susbtract_numbers(self):
        """Test subtracting stuff"""

        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
