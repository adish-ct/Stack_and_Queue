""" Create stack using two queue
    2 queue ---> FIFO converted
    stack ---> LIFO
"""


class Stack:
    def __init__(self, size):
        self.queue_1 = []
        self.queue_2 = []
        self.size = size

    def push(self, data):
        if len(self.queue_1) == self.size:
            print("stack is full".upper())
            return
        self.queue_1.append(data)

    def pop(self):
        if not self.queue_1:
            print("stack is empty".upper())
            return
        for _ in range(len(self.queue_1) - 1):
            self.queue_2.append(self.queue_1.pop(0))
        self.queue_1.pop()
        for _ in range(len(self.queue_2)):
            self.queue_1.append(self.queue_2.pop(0))

    def display(self):
        if not self.queue_1:
            print("stack is empty".upper())
            return
        print(self.queue_1)


s = Stack(5)
s.push(50)
s.push(60)
s.push(70)
s.push(80)
s.push(90)

s.pop()
s.pop()
s.pop()
s.pop()
s.push(90)
s.pop()


s.display()
