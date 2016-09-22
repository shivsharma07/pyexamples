'''
Created on Aug 12, 2016

@author: inssharma027
'''
N = int(raw_input().strip())

if N >= 1 and N <= 20:
    for i in xrange(N):
        print i**2

else:
    print "not in range"