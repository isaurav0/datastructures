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


tree1 = Tree()
tree1.insert(70)
tree1.insert(1)
tree1.insert(10)
tree1.insert(3)
tree1.insert(9)
tree1.insert(10)
tree1.insert(50)
tree1.insert(4)
print("Preorder traversal is: ")
tree1.preorder()
print("Postorder traversal is: ")
tree1.postorder()
print("Inorder traversal is: ")
tree1.inorder()
