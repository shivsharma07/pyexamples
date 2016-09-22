'''
Created on Aug 22, 2016

@author: inssharma027
'''
N = int(raw_input().strip())

s = raw_input().strip()

#li = [int(a) for a in s.split(" ")]

li = list(map(int, s.split(" ")))

print li[:N]
sumOfDiffVal = float(sum(set(li)))
avgOfnum = sumOfDiffVal/len(set(li))
print avgOfnum