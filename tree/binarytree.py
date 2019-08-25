import random

class Node:
    def __init__(self, val):
        self.value = val
        self.rightChild = None
        self.leftChild = None

    def insert(self, data):
        if(self.value == data):
            return False
        elif(self.value > data):
            if(self.leftChild):
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if(self.rightChild):
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def find(self, data):
        if(self.value == data):
            return True
        elif(self.value > data):
            if(self.leftChild):
                return self.leftChild.find(data)
            else:
                return False
        else:
            if(self.rightChild):
                return self.rightChild.find(data)
            else:
                return False

    #traversal
    def preorder(self):
        if(self):
            print(self.value)
            if(self.leftChild):
                self.leftChild.preorder()
            if(self.rightChild):
                self.rightChild.preorder()

    
    def postorder(self):
        if(self):
            if(self.leftChild):
                self.leftChild.postorder()
            if(self.rightChild):
                self.rightChild.postorder()
            print(self.value)
            
    def inorder(self):
        if(self):
            if(self.leftChild):
                self.leftChild.inorder()
            print(self.value)
            if(self.rightChild):
                self.rightChild.inorder()

    def getLevel(self, data, level):
        if(self.value==data):
            return level
        elif(self.value>data):
            if(self.leftChild):
                return self.leftChild.getLevel(data, level+1)
            else:
                return 'Element not found'
        else:
            if(self.rightChild):
                return self.rightChild.getLevel(data, level+1)
            else:
                return 'Element not found'

    def printTree(self, root):
        if(self):
            print("   "*root.getLevel(self.value,1),"", self.value)
            if(self.leftChild):
                self.leftChild.printTree(root)
            if(self.rightChild):
                self.rightChild.printTree(root)
            

    

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if(self.root):
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if(self.root):
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        if(self.root):
            return self.root.preorder()
        else:
            return False
    
    def postorder(self):
        if(self.root):
            return self.root.postorder()
        else:
            return False
    
    def inorder(self):
        if(self.root):
            return self.root.inorder()
        else:
            return False

    def getLevel(self, data):
        if(self.root):
            return self.root.getLevel(data,1)
        else:
            return 'Empty Tree'

    def printTree(self):
        return self.root.printTree(self.root)


tree1 = Tree()
for i in range(1,50):
    tree1.insert(random.randint(1,100))

# values = [5,3,6,1,0,2,8,7]
# for value in values:
#     tree1.insert(value)


# print("Preorder traversal is: ")
# tree1.preorder()
# print("Postorder traversal is: ")
# tree1.postorder()
# print("Inorder traversal is: ")
# tree1.inorder()

# data = 33
# print('level of %d is: '%data)
# print(tree1.getLevel(data))

tree1.printTree()
