
class Node(object):

    def __init__(self, data = None):
        self.data = data
        self.next = None

# single linked list
class linked_list(object):

    def __init__(self):
        self.head = Node()

    # Gives the size of the list
    def len(self):

        count = 0
        curr = self.head

        while curr.next != None:
            count += 1
            curr = curr.next

        return count

    # inserts new node at the last of the list
    def push(self, input):

        new_node = Node(input)
        curr = self.head

        while curr.next != None:
            curr = curr.next

        curr.next = new_node

    # removes given number if it's in linked list
    def pop(self, data):

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
test.push(20)
test.push(30)
test.push(40)
test.push(50)
test.push(60)
test.pop(30)

print(test.display())