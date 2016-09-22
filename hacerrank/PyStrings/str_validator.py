'''
Created on Aug 15, 2016

@author: Shiv Sharma
'''
s = raw_input().strip()
strLength = len(s)

if strLength > 0 and strLength < 1000:
    alphaNumFlag = alphaFlag = digitFlag = lowerFlag = upperFlag = False
    for l in s:
        if l.isalnum():
            alphaNumFlag = True
        if l.isalpha():
            alphaFlag = True
        if l.isdigit():
            digitFlag = True
        if l.islower():
            lowerFlag = True
        if l.isupper():
            upperFlag = True
    print alphaNumFlag
    print alphaFlag
    print digitFlag
    print lowerFlag
    print upperFlag
            