# Single linked list data structure

class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedList(object):

    def __init__(self):
        self.head = Node()

    def len(self):

        """Returns the size of the list"""

        count = 0
        curr = self.head

        while curr.next is not None:
            count += 1
            curr = curr.next

        return count

    def push(self, input):

        """Inserts new node in O(1) time"""

        new_node = Node(input)
        curr = self.head

        while curr.next is not None:
            curr = curr.next

        curr.next = new_node

    def pop(self, data):

        """Removes node in O(1) time"""

        curr = self.head
        nxt = curr.next
        size = self.len()
        count = False

        if size == 0:
            print("List is empty, please add some data!")

        elif size == 1 and nxt.data == data:
            curr.next == None
            count = True

        else:
            while curr.next.data != data:
                nxt = nxt.next
                curr = curr.next

            curr.next = nxt.next
            count = True

        if not count:
            print("Element not in the list.")

    def display(self):

        """Prints list elements"""

        output = []
        curr = self.head

        while curr.next != None:
            curr = curr.next
            output.append(curr.data)

        return output