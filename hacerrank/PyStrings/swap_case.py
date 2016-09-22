'''
Created on Aug 15, 2016

@author: Shiv Sharma
'''

s = raw_input().strip()
strLength = len(s)
swapStr = ""
if strLength > 0 and strLength <= 1000:
    for chr in s:
        if chr.islower():
            swapStr = swapStr + chr.upper()
        elif chr.isupper():
            swapStr = swapStr + chr.lower()
        else:
            swapStr = swapStr + chr
    print swapStr