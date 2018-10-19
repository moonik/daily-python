from data_structures.linked_list.node import Node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head is None

    def enqueue(self, value):
        node_ = Node(None, value)

        if self.empty():
            self.head = self.tail = node_
        else:
            self.tail.set_next(node_)
            self.tail = node_

    def dequeue(self):
        value = self.head.get_value()

        self.head = self.head.get_next()

        if self.head is None:
            self.tail = None

        return value
