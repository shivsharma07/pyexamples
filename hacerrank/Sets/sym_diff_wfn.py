'''
Created on Aug 22, 2016

@author: inssharma027
'''
n1 = int(raw_input().strip())
s1 = raw_input().strip()

n2 = int(raw_input().strip())
s2 = raw_input().strip()

a = set(list(map(int, s1.split(" "))))
b = set(list(map(int, s2.split(" "))))

fSet = a - b
fSet.update(b - a)
print sorted(fSet)

for i in sorted(fSet):
    print i


# a.union(b)
# #a.intersection(b)
# a.difference(b)
# b.difference(a)
# 
# print a
# print b



