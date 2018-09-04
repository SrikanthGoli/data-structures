
# Stack Data Structure
class Stack(object):

    """Stack data structure which provides
    insertion & Deletion at constant time - O(1)
    """

    def __init__(self):

        self.stack = []
        self.size = -1

    def len(self):

        return len(self.stack)

    def push(self, data):

        self.stack.append(data)
        self.size += 1

    def pop(self):

        self.stack.remove(self.stack[self.size])
        self.size -= 1

    def display(self):

        print(self.stack)