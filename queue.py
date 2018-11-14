class Node():
    __slots__ = 'data', 'link'

    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class queue():
    __slots__ = 'front', 'back'

    def __init__(self):
        self.front = None
        self.back = None

    def __str__(self):
        result = '< '
        temp_node = self.front
        while temp_node is not None:
            result += str(temp_node.data) + ' '
            temp_node = temp_node.link
        result += '>'
        return result

    def push(self, value):
        if self.back is None:
            self.front = self.back = Node(value)
        else:
            self.back.link = Node(value)
            self.back = self.back.link


    def pop(self):
        """
        pre: queue is not empty
        :return:
        """
        result = self.front.data
        self.front = self.front.link
        if self.front is None:
            self.back = None
        return result

    def is_empty(self):
        if self.front is None:
            return True
        return False

    def peek(self):
        """
        pre: queue is not empty
        :return:
        """
        if not self.is_empty():
            return self.front.data