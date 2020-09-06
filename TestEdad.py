# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import unittest
from Edad import edad

class PrU(unittest.TestCase):

    def test_edad(self):
        e=edad()
        result=e.E2070()
        self.assertEqual(result,52)


