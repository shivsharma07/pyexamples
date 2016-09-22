'''
Created on Aug 13, 2016

@author: Shiv Sharma
'''
n = int(raw_input().strip())
#nvalues = [int(x) for x in raw_input().split()][:n]
nvalues = raw_input().strip()
t = tuple(int(x) for x in nvalues.split()[:n])

print hash(t)