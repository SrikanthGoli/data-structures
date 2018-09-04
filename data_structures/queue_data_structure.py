# Queue Data Structure
class Queue(object):

    """Queue data structure which provides
    insertion & Deletion at constant time - O(1)
    """

    def __init__(self):

        self.queue = []

    # queue is empty check
    def is_empty(self):

        return self.size() == 0

    # returns the size of queue
    def size(self):

        return len(self.queue)

    # Adds element to queue
    def en_queue(self, data):

        self.queue.append(data)

    # removed element from queue
    def de_queue(self):

        return self.queue.pop(0)

    # display's the queue
    def display(self):

        return self.queue