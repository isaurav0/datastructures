class Queue:
    def __init__(self):
        self.line = []

    def append(self, value):
        self.line.append(value)

    def pop(self):
        self.line.pop(0)

    def show(self):
        print(self.line)

queue = Queue()
queue.append(3)
queue.append(2)
queue.append(4)
queue.show()
queue.pop()
queue.show()