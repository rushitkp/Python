#Write a program in python to implement Queue using Class and Methods and perform below operations.(Note: Use of object oriented paradigm is compulsory.)
#a) Create Queue
#b) Add an element
#c) Remove an element
#d) Merge two Queues
#e) List elements


class Queue:
    def __init__(self):
        self.queue = []

    def add_element(self, item):
        self.queue.append(item)

    def remove_element(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def merge(self, other_queue):
        self.queue.extend(other_queue.queue)

    def list_elements(self):
        return self.queue

# Create queues
queue1 = Queue()
queue2 = Queue()

# Add elements to queue1
queue1.add_element(1)
queue1.add_element(2)
queue1.add_element(3)

# Add elements to queue2
queue2.add_element(4)
queue2.add_element(5)
queue2.add_element(6)

# Remove element from queue1
print(queue1.remove_element())

# Merge queue2 into queue1
queue1.merge(queue2)

# List elements in queue1
print(queue1.list_elements())
