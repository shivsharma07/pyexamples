def getSublists(L, n):
    listofsublist = []
    lim = len(L)-n
    i = 0
    if n > 0:
        while i <= lim:
            sublist = L[i:i+n]
            listofsublist.append(sublist)
            i = i+1
    return listofsublist
    
#print getSublists([10, 4, 6, 8, 3, 4, 5, 7, 7, 2], 4)

def longestRun(L):
    lim = len(L)
    if lim == 1:
        return 1
    n = 1
    increasingList = []
    while n <= lim:
        for subList in getSublists(L, n):
            sublistLen = len(subList)
            i = 0
            while i < sublistLen-1:
                if subList[i] > subList[i+1]:
                    break
                elif i+2 == sublistLen:
                    increasingList = subList
                i = i +1
            #print " increasingList: "+str(increasingList)
        n = n+1        
    return len(increasingList)
print longestRun([10, 4, 6, 8, 3, 4, 5, 7, 7, 2])   
