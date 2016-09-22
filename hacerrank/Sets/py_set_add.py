'''
Created on Aug 22, 2016

@author: inssharma027
'''
n = int(raw_input().strip())
if n > 0 and n < 1000:
    countryList = set()
    for i in xrange(n):
        countryList.add(raw_input().strip())

    #print countryList
    print len(countryList)