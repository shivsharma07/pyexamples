#numOfDigits = 0
#def ndigits(number):
#    global numOfDigits
#    if number < 0:
#        number = -number
#    if number/10 > 0:
#        numOfDigits += 1
#        ndigits(number/10)
#    else:
#        numOfDigits += 1
#    return numOfDigits
    
def ndigits(number):
    def countNumberoFDigits(number, numOfDigits):
        if number < 0:
            number = -number
        if number/10 > 0:
            numOfDigits += 1
            return countNumberoFDigits(number/10, numOfDigits)
        else:
            numOfDigits += 1
            return numOfDigits
    return countNumberoFDigits(number, 0)
    
print ndigits(523142)
    
def f(n):
    if n == 1:
        return 1,0
    else:
        x, call_depth= f(n-1)
        return n * x, call_depth+1
        
print f(5)
        
print ndigits(322431)