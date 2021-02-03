class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def append(self, value):
        if not self.next:
            self.next = Node(value)
            return
        else:
            self.next.append(value)

    def traverse(self):
        if self.value:
            print(self.value, end=",")
        if self.next:
            self.next.traverse()

    def insertAt(self, depth, value, currentDepth):
        if currentDepth == depth:
            self.prev_next = self.next
            self.next = Node(value)
            self.next.next = self.prev_next
            return
        if depth > currentDepth and not self.next:
            print("Invalid range")
            return
        self.next.insertAt(depth, value, currentDepth + 1)

    def length(self, depth):
        if not self.next:
            return depth
        return self.next.length(depth + 1)

    def delete(self, currentDepth, index):

        if currentDepth == index:
            self.next = self.next.next
            print("deleting index: ", index)
            return True

        if not self.next:
            print("Out of range")
            return False

        self.next.delete(currentDepth + 1, index)


class SingleLinkedList:
    def __init__(self, logging=False):
        self.head = None
        self.logging = logging

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            if self.logging:
                print(f"+ Inserted {value} in head")
                print("-----------")
            return
        if self.logging:
            print("Starting from head")
        return self.head.append(value)

    def traverse(self):
        if not self.head:
            return
        self.head.traverse()

    def prepend(self, value):
        if not self.head:
            self.head = Node(value)
            return
        self.prev_head = self.head
        self.head = Node(value)
        self.head.next = self.prev_head
        return

    def insertAt(self, depth, value):
        if not self.head:
            self.head = Node(value)
            return
        self.head.insertAt(depth, value, 1)

    def length(self):
        if not self.head:
            return 0
        return self.head.length(1)

    def delete(self, index):
        if index == 0:
            self.head = self.head.next
            return True

        if index == 1:
            self.head.next = self.head.next.next
            return

        return self.head.next.delete(2, index)


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
s.prepend("678")
s.insertAt(5, "saurav")
s.traverse()
print("\n Length: ", s.length())

# delete(index)
s.delete(200)
print('\n')
s.traverse()
print("\n Length: ", s.length())

s.delete(2)
print('\n')
s.traverse()
print("\n Length: ", s.length())

s.delete(4)
print('\n')
s.traverse()
print("\n Length: ", s.length())
