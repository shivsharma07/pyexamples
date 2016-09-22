'''
Created on Aug 15, 2016

@author: Shiv Sharma
'''
import sys
N = int(raw_input().strip())
if N >= 2 and N <= 5:
    nested_list = []
    for i in xrange(2*N):
        if i % 2 == 0:
            name = raw_input().strip()
        else:
            score = float(raw_input().strip())            
            nested_list.append([name, score])    
    sec_low = low = sys.maxint
    nameList = []
    for li in nested_list:
        if li[1] < low:
            sec_low = low
            low = li[1]     
        elif (li[1] < sec_low and li[1] != low):
            sec_low = li[1]
    for li in nested_list:
        if li[1] == sec_low:
            nameList.append(li[0])
    nameList.sort()

    for e in nameList:
        print e
        