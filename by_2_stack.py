""" Create Queue using two stack
    2 stack ---> LIFO  method converted
    queue  ----> FIFO
"""

class Queue:
    def __init__(self, size):
        self.stack_1 = []
        self.stack_2 = []
        self.size = size

    def enqueue(self, data):
        if len(self.stack_1) == self.size:
            print("queue is full".upper())
            return
        self.stack_1.append(data)

    def dequeue(self):
        if not self.stack_1:
            print("queue is empty".upper())
            return
        for i in range(len(self.stack_1)):
            self.stack_2.append(self.stack_1.pop())
        self.stack_2.pop()
        for i in range(len(self.stack_2)):
            self.stack_1.append(self.stack_2.pop())

    def display(self):
        print(self.stack_1)


q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)

q.display()

