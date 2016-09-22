'''
Created on Jun 24, 2015

@author: Shiv Sharma
'''

def countOccurence(stringSentence, searchString):
    stringSentenceLength = len(stringSentence)
    searchStringLength = len(searchString)
    
    i= 0
    occurrenceCount = 0
    
    while(i <= stringSentenceLength+searchStringLength):
        if stringSentence[i:i+searchStringLength] == searchString:
            occurrenceCount = occurrenceCount + 1
            i = i + searchStringLength
        else:
            i = i+1
        while stringSentence[i-1:i+searchStringLength-1] == searchString and searchStringLength > 1:
            occurrenceCount = occurrenceCount + 1
            i = i + searchStringLength - 1
        
    return occurrenceCount
            
#print countOccurence('qwaabobobobxaxsaabobobzzzbobbob', 'bob')

def longestAlphabeticSubstring(stringSentence):
    stringSentenceLength = len(stringSentence)
    longestSubstring = ''
    longestSubstringLength = 0
    newLongestSubstring = ''
    newLongestSubstringLength = 0
    
    i = 0
    #print stringSentenceLength
    while i < stringSentenceLength:
        j = i        
        if newLongestSubstringLength < longestSubstringLength:
            newLongestSubstringLength = longestSubstringLength
            newLongestSubstring = longestSubstring
            longestSubstringLength = 0
            longestSubstring = ''
        while j < stringSentenceLength - 1:
            if len(longestSubstring) > 0 and longestSubstring[j] <= stringSentence[j]:
                longestSubstring += stringSentence[j]
            else:
                break
            j = j +1
        
        longestSubstringLength = len(longestSubstring)                   
        i = i + 1
        
    print newLongestSubstring
    print newLongestSubstringLength
    
    return None
    
longestAlphabeticSubstring('aaabcazdrafghijklmnaqwa')
    
        