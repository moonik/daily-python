class Node:
    def __init__(self, next=None, value=None):
        self.next = next
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value