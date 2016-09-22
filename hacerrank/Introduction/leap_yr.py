'''
Created on Aug 12, 2016

@author: inssharma027
'''

def is_leap(year):
    leap = False
    
    if year >= 1900 and year <= 10**5: 
        if year%4 == 0:        
            if not (year%100 == 0 and year%400 != 0):
                leap = True
    return leap

year = int(raw_input())
print is_leap(year)