'''
Created on Aug 29, 2016

@author: Shiv Sharma
'''
s = raw_input().strip()
print s[:].split()
for x in s[:].split():
    #s = s.replace(x, x.capitalize())
    s = s.replace(x, x.title())
print(s)