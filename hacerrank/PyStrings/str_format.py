'''
Created on Aug 16, 2016

@author: inssharma027
'''
#http://stackoverflow.com/questions/3228865/python-how-do-i-format-a-number-with-a-variable-number-of-digits
#https://infohost.nmt.edu/tcc/help/pubs/python/web/format-var-length.html
#https://mkaz.tech/python-string-format.html

N = int(raw_input().strip())
formatWidth = len(bin(N)) - 2
for i in xrange(N):
    #print "%5s %5s %5s %5s" %(i+1, oct(i+1).lstrip('0'), '{:X}'.format(i+1), '{:b}'.format(i+1))
    #print "%*s" %(formatWidth,i+1), "%*s" %(formatWidth, oct(i+1).lstrip('0')), "%*s" %(formatWidth, '{:X}'.format(i+1)), "%*s" %(formatWidth, '{:b}'.format(i+1))
    #print "%{width} {0} %{width} {1} %{width} {2} %{width} {3}" .format(i+1, oct(i+1).lstrip('0'), '{:X}'.format(i+1), '{:b}'.format(i+1), width=formatWidth)
    
    #print "{0:{fill}{width}d} {0:{fill}{width}X} {0:{fill}{width}o} {0:{fill}{width}b} ".format(i, fill= ' ', width=formatWidth)
    
    print "{0:>{width}d} {0:>{width}o} {0:>{width}X} {0:>{width}b} ".format(i+1, width=formatWidth)