'''
Created on Aug 12, 2016

@author: inssharma027
'''

a = int(raw_input().strip())
b = int(raw_input().strip())

if (a >= 1 and a <= 10**10)  and (b >= 1 and b <= 10**10):
    print a + b
    print a - b
    print a * b
else:
    print "not in range"
