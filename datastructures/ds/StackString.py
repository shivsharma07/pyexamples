'''
Created on May 2, 2015

@author: shiv.sharma
'''
from ds.Stack import Stack
class StackString:
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.originalString = ""
    
    def isStringEmpty(self, originalString):
        return originalString == ""
    
    def reverseString(self, originalString):
        stk = Stack()
        
        for i in originalString:
            stk.push(i)
        
        print(stk.items)
        
        while not stk.isEmpty():
            print(stk.pop())
        
    
obj = StackString()
print(obj.originalString)
print(obj.isStringEmpty("Test"))
obj.reverseString("Shiv")