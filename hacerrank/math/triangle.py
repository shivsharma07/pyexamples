'''
Created on Aug 29, 2016

@author: Shiv Sharma
'''
for i in range(1,int(raw_input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    #print "".join(map(str, range(1,i+1))) + "".join(map(str, range(i-1, 0, -1)))
    
    print ((10**i-1)/9)**2