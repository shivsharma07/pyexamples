'''
Created on Dec 27, 2015

@author: Shiv Sharma
'''


def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    
    while first <= last and not found:
        midpoint = (first+last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if alist[midpoint] < item:
                first = midpoint + 1
            else:
                last = midpoint - 1
    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))

def binarySearchRecursive(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] < item:
            binarySearchRecursive(alist[midpoint+1:], item)
        else:
            binarySearchRecursive(alist[:midpoint], item)
            
tlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))