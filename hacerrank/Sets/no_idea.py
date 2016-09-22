'''
Created on Aug 22, 2016

@author: inssharma027
'''
nm = raw_input().strip()
arr = raw_input().strip()
a = raw_input().strip()
b = raw_input().strip()

n, m = [int(x) for x in nm.split(" ")]
arr = list(map(int, arr.split(" ")))
a = set(list(map(int, a.split(" "))))
b = set(list(map(int, b.split(" "))))

result = 0
for e in arr:
    if e in a:
        result = result + 1
    if e in b:
        result = result - 1

print result