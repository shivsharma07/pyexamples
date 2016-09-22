class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree(Node):
    def __init__(self):
        self.root = None

    def addNode(self,data):
        return Node(data)

    def insert(self,root,data):
        if(root == None):
            root = self.addNode(data)
        else:
            if(data <= root.data):
                root.left = self.insert(root.left,data)
            else:
                root.right = self.insert(root.right,data)
        return root

    def PreOrder(self,root):
        if root == None:
            pass
        else:
            print(root.data)
            self.PreOrder(root.left)
            self.PreOrder(root.right)
            
    def PostOrder(self,root):
        if root == None:
            pass
        else:
            print(root.data)
            self.PostOrder(root.left)
            self.PostOrder(root.right)