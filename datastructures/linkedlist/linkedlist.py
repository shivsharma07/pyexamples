'''
Created on Dec 20, 2015

@author: Shiv Sharma
'''

class Node:
    '''
    classdocs
    '''

    def __init__(self, initdata):
        '''
        Constructor
        '''
        self.data = initdata
        self.next = None
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata
    
    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
     
    def __init__(self):
        self.head = None
         
    def isEmpty(self):
        return self.head == None
     
    def printList(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()
 
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
     
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            #print(current.getData())
            current = current.getNext()
             
        return count
     
    def search(self, item):
        current = self.head
        found = False
         
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()                
        return found
     
    def remove(self, item):
        current = self.head
        previous = None
        found = False
         
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
         
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
             
    def reverseList(self):
        previous = None
        current = self.head
        next = None
          
        while current != None:            
            next = current.getNext()
            current.setNext(previous)
            previous = current
            current = next
        self.head = previous
         
    def append(self, item):
        current = self.head
        while current != None:
            if current.getNext() == None:
                temp = Node(item)
                current.setNext(temp)
                return temp
            
            current = current.getNext()
        
class OrderedList:
        
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def printList(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()
    
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not stop and not found:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext() 
        return found
    
    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True                
            else:
                previous = current
                current = current.getNext()
        
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
            
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        stop = False
        
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()       
        if found == True:
            previous.setNext(current.getNext())
        elif current == None and found == False:
            print("Node does not exist in the list.") 
myorderedList = OrderedList()
myorderedList.add(2)
myorderedList.add(5)
myorderedList.add(4)
myorderedList.add(7)
myorderedList.printList()
print(myorderedList.search(7))
myorderedList.remove(9)
myorderedList.printList()
    
    
    
    
# mylist = UnorderedList()
# mylist.add(31)
# mylist.add(77)
# mylist.add(17)
# mylist.add(93)
# mylist.add(26)
# mylist.add(54)
# print(mylist.size())
# print(mylist.search(93))
# mylist.remove(93)
# print(mylist.size())
# mylist.printList()
# mylist.append(131)
# mylist.append(132)
# print("-"*50)
# mylist.reverseList()
# mylist.printList()