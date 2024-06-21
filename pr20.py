#Write a program in python to implement Stack using Class and Methods and perform below operations.(Note: Use of object oriented paradigm is compulsory.)
#a) Create Stack
#b) Pop
#c) Push
#d) Merge two stack
#e) List element


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def merge(self, other_stack):
        self.stack.extend(other_stack.stack)

    def list_elements(self):
        return self.stack

# Create stacks
stack1 = Stack()
stack2 = Stack()

# Push elements onto stack1
stack1.push(1)
stack1.push(2)
stack1.push(3)

# Push elements onto stack2
stack2.push(4)
stack2.push(5)
stack2.push(6)

# Pop element from stack1
print(stack1.pop())

# Merge stack2 into stack1
stack1.merge(stack2)

# List elements in stack1
print(stack1.list_elements())
