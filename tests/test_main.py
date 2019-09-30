"""
unit test for admin.py
"""

import unittest
from admin import main


class AdminTest(unittest.TestCase):
    """
        unit test class
    """

    def setUp(self):
        """
            set up unit test
        """
        pass

    def test_flask_app_exists(self):
        """
            test unittest 2
        """

        self.assertTrue('APP' in dir(main))
