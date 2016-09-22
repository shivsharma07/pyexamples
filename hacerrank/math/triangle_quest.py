'''
Created on Aug 29, 2016

@author: Shiv Sharma
'''
for i in range(1,input()):
    #print ("%d" % i) * i
    print sum(map(lambda x: i * 10**x, xrange(i)))