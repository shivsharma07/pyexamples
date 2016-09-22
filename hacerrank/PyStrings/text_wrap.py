'''
Created on Aug 16, 2016

@author: Shiv Sharma
'''
s = raw_input().strip()
w = int(raw_input().strip())

strLength = len(s)
if (strLength > 0 and strLength < 1000) and (w > 0 and w < strLength):
    import textwrap
    print textwrap.fill(s,w)
 