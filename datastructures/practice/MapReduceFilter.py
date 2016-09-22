'''
Created on Sep 16, 2015

@author: Shiv Sharma
'''

def sqrt(x):
    return x**2

def cube(x):
    return x**3

fSeq = [sqrt, cube]

for r in range(5):
    print (list(map(lambda x : x(r), fSeq)))
    
#filter
print(list(filter(lambda x: x%2 == 0, range(-10,5))))

#reduce
def myReduce(func, seq):
    tally = seq[0]
    for next in seq[1:]:
        tally = func(next, tally)
        #print (tally)
    return tally

#print (myReduce(lambda x,y : x*y, [1,2,3,4]))
print (myReduce(lambda x,y : x/y, [1,2,3,4]))