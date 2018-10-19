from data_structures.linked_list.node import Node


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def size(self):
        return self.size

    def empty(self):
        return self.size == 0

    def value_at(self, index):
        if index < 0 or index >= self.size:
            return None

        current = self.head

        while index is not 0:
            current = current.get_next()
            index -= 1

        return current.get_value()

    def push_front(self, value):
        self.head = Node(self.head, value)
        self.size += 1

    def pop_front(self):
        if self.empty():
            return None

        value = self.head.get_value()
        self.head = self.head.get_next()

        if self.head is None:
            self.tail = None

        self.size -= 1

        return value

    def push_back(self, value):
        node_ = Node(None, value)
        if self.empty():
            self.head = node_
            self.tail = node_
        else:
            self.tail.set_next(node_)
            self.tail = node_
        self.size += 1

    def pop_back(self):
        if self.empty():
            return None

        current = self.head

        while current.get_next() is not None:
            next_ = current.get_next()
            if next_ == self.tail:
                value = next_.get_value()
                current.set_next(None)
                self.tail = current
                self.size -= 1
                return value
            current = current.get_next()
        return self.pop_front()

    def front(self):
        return self.head.get_value()

    def back(self):
        return self.tail.get_value()

    def insert(self, index, value):
        if index < 0 or index >= self.size:
            return

        new_node = Node(None, value)

        if index == 0:
            new_node.set_next(self.head)
            self.head = new_node
            self.size += 1
            return

        current = self.head

        while index-1 is not 0:
            current = current.get_next()
            index -= 1

        current_next = current.get_next()
        new_node.set_next(current_next)
        current.set_next(new_node)

        if new_node.get_next() is None:
            self.tail = new_node

        self.size += 1

    def erase(self, index):
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.pop_front()
            return

        if index == self.size-1:
            self.pop_back()
            return

        current = self.head

        while index-1 is not 0:
            index -= 1
            current = current.get_next()

        current.set_next(current.get_next().get_next())
        self.size -= 1

        if current.get_next() is None:
            self.tail = current

    def value_n_from_end(self, n):
        if n < 0 or n >= self.size:
            return None

        if n == 0:
            return self.tail.get_value()
        elif n == self.size-1:
            return self.head.get_value()

        current = self.head

        while n is not 0:
            current = current.get_next()
            n -= 1

        return current.get_value()

    def remove_value(self, value):
        if self.head.get_value() == value:
            self.pop_front()
        elif self.tail.get_value() == value:
            self.pop_back()
        else:
            current = self.head
            while current.get_next() is not None:
                if current.get_value() == value:
                    current.set_next(current.get_next().get_next())
                    if current.get_next() is None:
                        self.tail = current

    def reverse(self):
        if self.empty():
            return

        prev = None
        current = self.head
        self.tail = current

        while current is not None:
            next_ = current.get_next()
            current.set_next(prev)
            prev = current
            current = next_
        self.head = prev
