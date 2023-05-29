# strcture of queue

queue = []
# queue.append(10)
# queue.append(20)
# queue.append(30)
# queue.append(40)
# queue.append(50)
#
# a = queue.pop(0)
# print("Removed elements :", a)
# a = queue.pop(0)
# print("Removed elements :", a)

# queue.insert(0, 10)
# queue.insert(0, 20)
# queue.insert(0, 30)
# queue.insert(0, 40)
# queue.insert(0, 50)
#
# a = queue.pop()
# print("removed element :", a)
# a = queue.pop()
# print("removed element :", a)
#
# print(queue)


""" queue implementation using class and object
    enqueue : append() or insert(0, data)
    dequeue : pop(0) or pop()
"""
#
# class Queue:
#     def __init__(self, size):
#         self.queue = []
#         self.size = size
#
#     def enqueue(self, data):
#         if len(self.queue) == self.size:
#             print("queue is full..".upper())
#             return
#         self.queue.append(data)
#
#     def dequeue(self):
#         if not self.queue:
#             print("queue is empty..".upper())
#             return
#         self.queue.pop(0)
#
#     def is_empty(self):
#         if not self.queue:
#             print("empty queue")
#             return
#         print("you can take operations on the queue".upper())
#
#     def display(self):
#         if self.is_empty():
#             return
#         print(self.queue)
#
#
# que = Queue(5)
# que.enqueue(10)
# que.enqueue(20)
# que.enqueue(30)
# que.enqueue(40)
# que.enqueue(50)
#
# que.dequeue()
# que.dequeue()
# que.dequeue()
#
#
# que.display()

""" Queue implementation using dequeue- double ended queue module collection
    append() : enqueue
    popleft() : dequeue
    
    pop()   : dequeue
    appendleft() : enqueue
"""
#
# import collections
#
#
# class Queue:
#     def __init__(self, size):
#         self.queue = collections.deque()
#         self.size = size
#
#     def enqueue(self, data):
#         # by using append method
#         if len(self.queue) == self.size:
#             print("queue is full".upper())
#             return
#         self.queue.append(data)
#
#         #by using appendleft method.
#         # if len(self.queue) == self.size:
#         #     print("queue is full".upper())
#         #     return
#         # self.queue.appendleft(data)
#
#     def dequeue(self):
#         # by using popleft method
#         if self.is_empty():
#             return
#         self.queue.popleft()
#
#         #by using pop method
#         # if self.is_empty():
#         #     return
#         # self.queue.pop()
#
#     def is_empty(self):
#         if not self.queue:
#             print("queue is empty..".upper())
#             return
#         print("you can take operations on the queue")
#
#     def display(self):
#         if not self.queue:
#             return
#         print(self.queue)
#
#
# q = Queue(5)
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)
# q.enqueue(50)
#
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
#
# q.display()

""" Queue implemented using Queue module
    enqueue : put()
    display : get()
    
"""

import queue


class Queue:
    def __init__(self, size):
        self.queue_list = queue.Queue(maxsize=size)
        self.size = size

    def put(self, data):
        if self.queue_full():
            return
        self.queue_list.put(10, timeout=1)

    def get(self):
        if self.is_empty():
            return
        print(self.queue_list.get(timeout=1))

    def is_empty(self):
        if not self.queue_list:
            print("queue is empty".upper())
            return True

    def queue_full(self):
        if self.queue_list.full():
            print("Queue is full".upper())
            return True

    def display(self):
        if self.is_empty():
            return
        print(self.queue_list)




q = queue.Queue()
q.put(20)
q.put(30)
q.put(40)
q.put(50)


print(q.get(timeout=1))
print(q.get(timeout=1))
print(q.get(timeout=1))
print(q.get(timeout=1))

