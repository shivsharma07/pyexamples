'''
Created on Aug 23, 2016

@author: inssharma027
'''
k = int(raw_input().strip())
if k > 1 and k < 1000:
    s = raw_input().strip()
    s = list(map(int, s.split(" ")))

myset = set(s)
print sum(s)
print sum(myset)*k
print ((sum(myset)*k)-(sum(s)))//(k-1)
