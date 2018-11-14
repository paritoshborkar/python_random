class Node():
   __slots__ = 'data','link'

   def __init__(self, data, link = None):
       self.data = data
       self.link = link

class stack():
    __slots__ = 'top'

    def __init__(self):
        self.top = None

    def __str__(self):
        result = '< '
        temp_node = self.top
        while temp_node is not None:
            result += str(temp_node.data)
            result += ' '
            temp_node = temp_node.link
        result += '>'
        return result

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if not self.is_empty():
            result = self.top.data
            self.top = self.top.link
            return  result

    def is_empty(self):
        if self.top is None:
            return True
        return False

    def peek(self):
        if not self.is_empty():
            return self.top.data
