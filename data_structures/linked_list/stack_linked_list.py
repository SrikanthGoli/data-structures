
# Stack data structure using linked list.
class Node(object):

    def __init__(self, data = None):

        self.data = data
        self.next = None

class StackLinkedList(object):

    """Stack data structure which provides
    insertion & Deletion at constant time - O(1)
    """

    def __init__(self, data):

        self.root = Node(data)

    def push(self, data):

        new_node = Node(data)
        new_node.next = self.root
        self.root = new_node

    def pop(self):

        self.root = self.root.next

    def display(self):

        res = []
        curr_node = self.root

        while curr_node is not None:
            res.append(curr_node.data)
            curr_node = curr_node.next

        return res