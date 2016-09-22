def isPalindrome(aString):
    '''
    aString: a string
    '''
    n = len(aString)
    for ltr in aString:
        if ltr == aString[n-1]:
            n = n-1
        else:
            return False
    return True
    
print isPalindrome("abc")
            