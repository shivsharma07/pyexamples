'''
Created on Aug 16, 2016

@author: Shiv Sharma
'''
N, M = map(int,raw_input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in xrange(1,N,2): 
    print (M-i-i*2)/2*"-" + i*".|."+(M-i-i*2)/2*"-"
print (M-7)/2*"-"+"WELCOME"+(M-7)/2*"-"
for i in xrange(N-2,-1,-2): 
    print (M-i-i*2)/2*"-" + i*".|."+(M-i-i*2)/2*"-"