

import unittest
from punto3 import punto

class pru(unittest.TestCase):


    def test_desco(self):
        e=punto()
        result= e.descomponer()
        print(result)
        self.assertEqual(result,"h")

