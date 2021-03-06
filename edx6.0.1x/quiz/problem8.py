def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    #for i,x in enumerate(L):
    #    if not f(x):                        
    #        L.remove(x)
    #return len(L)
        
    L[:] = [x for x in L if f(x)]
    return len(L)
def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a', 'cdf', 'bca', 'bca', 'cdf', 'b']
print satisfiesF(L)
print L