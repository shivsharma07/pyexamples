s = 'azcbobobegghakl'
searchTerm = 'bob'
i = 0
searchTermCount = 0
for letter in s:
    if searchTerm == s[i:i+len(searchTerm)]:
        searchTermCount += 1
    i += 1
print 'Number of times bob occurs is: '+str(searchTermCount)