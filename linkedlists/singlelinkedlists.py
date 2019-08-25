class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, nextNode):
        self.next = nextNode



class linkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        current = self.head
        if(current):
            while current.getNext() !=None:
                current = current.getNext()
            current.setNext = newNode
        else:
            newNode.setNext = None
            self.head = newNode

    def traverse(self):
        current = self.head
        #     current = current.getNext()
        while(True):
            print(current.getData())
            if(current.getNext()):
                current = current.getNext()
            else:
                break


list1 = linkedList()
list1.insert(5)
list1.insert(10)
list1.insert(15)
list1.insert(20)
list1.insert(25)
list1.insert(35)
list1.traverse()