'''
Created on Apr 9, 2016

@author: Shiv Sharma
'''
def GCD(a, b):
    if 0 == a or 0 == b:
        return -1
    if 1 == a or 1 == b:
        return 1
    while 0 < a and 0 < b:
        if a > b:
            a %= b
        else:
            b %= a
    return 0 == a and b or a

import unittest

