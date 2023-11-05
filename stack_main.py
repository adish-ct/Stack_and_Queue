# create stack using List concept

#
# stack = []
# stack.append(10)
# stack.append(20)
# stack.append(30)
# stack.append(40)
# stack.append(50)
#
# stack.pop()
#
# print(stack[-1])
# print(stack)

# Time Complexity

#    push - O(1)
#    pop  - O(1)
#    peek  - O(1)
#    is_empty - O(1)


class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, data):
        length = len(self.stack)
        if length == self.size:
            print("Stack is full")
            return
        return self.stack.append(data)

    def pop(self):
        length = len(self.stack)
        if not self.stack:
            print(self.is_empty())
            return
        return self.stack.pop()

    def top_element(self):
        if not self.stack:
            print("Stack is empty....")
            return
        return self.stack[-1]

    def is_empty(self):
        print("Stack is empty..")
        return


stack_data = Stack(10)
stack_data.push(52)
stack_data.push(55)
stack_data.push(56)
stack_data.pop()
stack_data.pop()
stack_data.pop()
stack_data.pop()


""" stack using deque methode """
#
# from collections import deque
#
# class Stack:
#     def __init__(self, size):
#         self.stack = collections.deque()
#         self.size = size
#
#     def push(self, data):
#         if len(self.stack) == self.size:
#             print("Stack is full".upper())
#             return
#         self.stack.append(data)
#
#     def pop(self):
#         if len(self.stack) == 0:
#             print("Stack is empty".upper())
#             return
#         self.stack.pop()
#
#     def display(self):
#         print(self.stack)
#
#     def peek(self):
#         print("The element present in the top of the stack :".upper(), self.stack[-1])
#
#
# st = Stack(5)
# st.push(30)
# st.push(40)
# st.push(80)
# st.push(60)
# st.push(50)

# st.display()
# st.peek()

""" Stack creating using Lifo Queue in Queue collection"""

from queue import LifoQueue


class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = LifoQueue()
        self.length = self.stack.qsize()
        print(self.stack)

    def put(self, data):
        if self.length == self.size:
            print("stack is full ...".upper())
            return
        self.stack.put(data)

    def pop(self):
        if self.is_empty():
            print("stack is empty ... ".upper())
        self.stack.get()

    def is_empty(self):
        if self.stack.empty():
            return True

    def display(self):
        if self.is_empty():
            print("Stack is empty , add elements using put method.".upper())
        print(self.stack)


st = Stack(5)
st.put(30)
st.put(40)
st.put(50)
st.put(60)
print(st.put(70))
