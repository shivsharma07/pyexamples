'''
Created on Aug 14, 2016

@author: Shiv Sharma
'''
import sys
n = int(raw_input().strip())
in_arr = [int(x) for x in raw_input().split()][:n]

max = sec_max = -sys.maxint - 1
 
for ele in in_arr:
    if ele > max:
        sec_max = max
        max = ele
    else:
        if ele > sec_max and ele != max:
            sec_max = ele
print sec_max
print max

#second maximum
# uList = list(set(in_arr))
# print uList
# uList.sort()
# if len(uList) >= 2:
#     print uList[-2]