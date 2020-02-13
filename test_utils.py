# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        # À compléter...
        self.assertEqual(utils.fact(3), 6)
    
    def test_roots(self):
        # À compléter...
        self.assertEqual(utils.roots(1,-4,3),(1,3))
    
    def test_integrate(self):
        # À compléter...
        self.assertEqual(utils.integrate('x**2 - 1',-1,1),-1.333,3)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
