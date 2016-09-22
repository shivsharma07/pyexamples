'''
Created on Aug 12, 2016

@author: inssharma027
'''
N = int(raw_input().strip())

if(N >= 1 and N <= 100):
    if N%2 != 0:
        print "Weird"
    else:
        if N in range(2,6):
            print "Not Weird"
        elif N in range(6,21):
            print "Weird"
        elif N > 20:
            print "Not Weird"
else:
    print "greater"