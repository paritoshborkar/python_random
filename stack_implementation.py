class Node():
    __slots__ = 'data', 'link'

    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class Stack():
    __slots__ = 'top', 'size'

    def __init__(self):
        self.top = None
        self.size = 0

    def __str__(self):
        result = '< '
        temp_node = self.top
        while temp_node is not None:
            result += str(temp_node.data) + ' '
            temp_node = temp_node.link
        result += '>'
        return result

    def push(self, value):
        self.top = Node(value, self.top)
        self.size += 1

    def pop(self):
        if not self.is_empty():
            result = self.top.data
            self.top = self.top.link
            self.size -= 1
            return result

    def is_empty(self):
        if self.top is None:
            return True
        return False

    def peek(self):
        if not self.is_empty():
            return self.top.data

    def __sizeof__(self):
        return self.size

