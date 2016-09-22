'''
Created on Aug 3, 2015

@author: Shiv Sharma
'''
import sys
import practice
from _csv import writer

print(sys.path)
print(dir(practice))

def raising_python_eception(x,y):
    try:
        z = x/y
        print z
    except ZeroDivisionError,e:
        err = e
        print e

raising_python_eception(15, 5)

def writer():
    title = 'Sir'
    name = (lambda x: title+' '+x)
    return name

who = writer()

print(who('Shiv Sharma'))
 

if __name__ == '__main__':
    pass