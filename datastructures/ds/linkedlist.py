'''
Created on May 1, 2015

@author: shiv.sharma
'''
class Node:
    def __init__(self, data):
        self.previous = None
        self.next = None
        self.data = data
        
class LinkedList(Node):
    '''
    classdocs
    '''
    def __init__(self, params):
        '''
        Constructor
        '''
        self.data = None
        