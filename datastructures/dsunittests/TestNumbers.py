'''
Created on Apr 9, 2016

@author: Shiv Sharma
'''
import unittest

from algorithms import numbers as algorithm
class TestNumbers(unittest.TestCase):
    '''
    Unit test case for numbers
    '''
    
    def testGCD(self):
        self.assertEquals(8, algorithm.GCD(24, 16))
        self.assertEquals(8, algorithm.GCD(16, 24))
        self.assertEquals(16, algorithm.GCD(16, 16))
        self.assertEquals(1, algorithm.GCD(13, 29))
        

if __name__ == "__main__":
#     objTest = TestNumbers()
#     objTest.testGCD()
    unittest.main()