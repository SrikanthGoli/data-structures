
class Node(object):

    def __init__(self, data = None):
        self.data = data
        self.next = None

# single linked list
class linked_list(object):

    def __init__(self):
        self.head = Node()

    # inserts new node at the last of the list
    def push(self, input):

        new_node = Node(input)
        curr = self.head

        while curr.next != None:
            curr = curr.next

        curr.next = new_node

    # returns the elements in a list
    def display(self):

        output = []
        curr = self.head

        while curr.next != None:
            curr = curr.next
            output.append(curr.data)

        return output


test = linked_list()
test.push(10)
print(test.display())