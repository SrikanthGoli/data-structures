# Implementing Queues data structure using linked list

class Node(object):

    def __init__(self, data=None):

        self.data = data
        self.next = None

class Queue(object):

    """Queue data structure which provides
    insertion & Deletion at constant time - O(1)
    """

    def __init__(self, data):

        self.root = Node(data)

    def en_queue(self, data):

        new_node = Node(data)
        new_node.next = self.root
        self.root = new_node

    def de_queue(self):

        prev_node = self.root
        curr_node = prev_node.next

        if prev_node.next is None:
            self.root = None

        else:
            while curr_node.next is not None:
                prev_node = curr_node
                curr_node = curr_node.next

            prev_node.next = None

    def display(self):

        res = []
        curr_node = self.root

        while curr_node is not None:
            res.append(curr_node.data)
            curr_node = curr_node.next

        return res