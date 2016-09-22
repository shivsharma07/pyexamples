'''
Created on Aug 23, 2016

@author: inssharma027
'''
n1 = int(raw_input().strip())
s1 = raw_input().strip()

n2 = int(raw_input().strip())
s2 = raw_input().strip()

s1 = set([int(x1) for x1 in s1.split(" ")])
s2 = set([int(x2) for x2 in s2.split(" ")])

print len(s1.union(s2))
print s1
print s2
print s1.union(s2)
