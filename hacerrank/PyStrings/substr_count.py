'''
Created on Aug 15, 2016

@author: Shiv Sharma
'''
s = raw_input().strip()
substr = raw_input().strip()
strLength = len(s)
if strLength >= 1 and strLength <= 200:
    substrCount = 0
    substrLength = len(substr)
    for i in range(0, strLength-substrLength+1):
        if s[i:i+substrLength] == substr:
            substrCount = substrCount + 1
    print substrCount