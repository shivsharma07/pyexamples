class Node:
    def __init__(self,data):
        self.data = data
        self.next= None

class List:
    def __init__(self):
        self.firstNode = Node(None)

    def inserthead(self,newnode):
        if not self.firstNode.next:
            newnode.next = None
            self.firstNode.next = newnode
        else:
            newnode.next = self.firstNode.next
            self.firstNode.next= newnode

    def __show(self,start):
        if start.next:
            print start.data
            self.__show(start.next)

    def printlist(self):
        self.__show(self.firstNode)

    def __reverte_recursive(self,node):
        temp = None
        if not node.next: return node
        else:
            temp = self.__reverte_recursive(node.next)
            node.next.next= node
            node.next = None
        return temp

    def reverte_list1(self):
        self.firstNode=self.__reverte_recursive(self.firstNode)

    def __reverte_iterative(self,node):
        temp = None
        previous = None
        while node and node.next:
            temp = node.next
            node.next= previous
            previous = node
            node = temp
        return previous
    def reverte_iterative(self):
        self.firstNode=self.__reverte_iterative(self.firstNode)

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")


list1= List()

list1.inserthead(nodeA)
list1.inserthead(nodeB)
list1.inserthead(nodeC)
list1.inserthead(nodeD)
list1.inserthead(nodeE)


print "list"
list1.printlist()
print "list reverse"
list1.reverte_list1()
list1.printlist()
list1.reverte_iterative()
print "list reverse reverse"
list1.printlist()