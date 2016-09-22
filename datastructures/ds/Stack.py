'''
Created on May 2, 2015

@author: shiv.sharma
'''
class Stack:
    '''
    Stack implementation in python
    '''
    _items = None #protected

    def __init__(self):
        '''
        Constructor
        '''
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        return self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

#===============================================================================
# s = Stack()
# print(s.isEmpty())
# s.push(4)
# s.push(1)
# s.pop()
# s.push(True)
# s.push('Shiv')
# print(s.peek())
# print(s.items)
# s.push(8.4)
# print(s.size())
# print(s.isEmpty())
# while not s.isEmpty():
#     s.pop()
# print(s.items)
#===============================================================================