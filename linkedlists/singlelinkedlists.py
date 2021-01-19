class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def append(self, value):
        if not self.next:
            self.next = Node(value)
            print(f"+ Inserted {value} in tail")
            print("-----------")
            return
        else:
            self.next.append(value)
            print("Calling next node")

    def traverse(self):
        if self.value:
            print(self.value, end=",")
        if self.next:
            self.next.traverse()


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            print(f"+ Inserted {value} in head")
            print("-----------")
            return
        print("Starting from head")
        return self.head.append(value)

    def traverse(self):
        if not self.head:
            return
        self.head.traverse()



    # def traverse(self):

s = SingleLinkedList()
s.append("20")
s.append("30")
s.append("40")
s.append("50")
s.append("60")
s.append("70")
s.append("80")
s.append("90")
s.append("100")
s.append("1")
s.append("2")

s.traverse()

# append into linked list: 
# appendions.append("20")

# Find length of linkedlist:
# s.length()

# Get second element
# s.get(2)

