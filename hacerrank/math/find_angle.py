'''
Created on Aug 29, 2016

@author: Shiv Sharma
'''
import math
AB = int(raw_input())
BC = int(raw_input()) 
print str(int(round(math.degrees(math.atan2(AB,BC)))))+'°'