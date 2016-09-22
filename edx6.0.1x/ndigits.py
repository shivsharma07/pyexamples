def ndigits(x):
    if x < 0:
        x = -x
    if x > -10 and x < 10:
        return 1
    if x/10 > 0:
        numOfDigits = ndigits(x/10)
        return numOfDigits+1
        
print ndigits(-1322132)