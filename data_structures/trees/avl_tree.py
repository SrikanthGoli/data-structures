# AVL Tree data structure

class Node(object):

    def __init__(self, data = None):

        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.height = None


class AvlTree(object):

    def __init__(self, data=None):

        """Performs insert, delete, search in O(logN)."""

        self.root = Node(data)

    def avl_push(self, data):

        """Inserts new node in O(logn) time."""

        new_node = Node(data)
        curr_node = self.root
        prev_node = None

        while curr_node:
            prev_node = curr_node

            if data < curr_node.data:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        new_node.parent = prev_node

        if data < prev_node.data:
            prev_node.left = new_node
        else:
            prev_node.right = new_node

        self.rebalance(new_node)

    def min(self, root):

        """Returns the min element from the given root."""

        curr_node = root

        while curr_node.left:
            curr_node = curr_node.left

        return curr_node.data

    def max(self, root):

        """Returns the max element from the given root."""

        curr_node = root

        while curr_node.right:
            curr_node = curr_node.right

        return curr_node.data

    def lookup(self, data):

        """Returns the Node of the given input."""

        curr_node = self.root

        while curr_node != data:
            if data < curr_node.data:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        return curr_node

    def successor(self, data):

        """Returns the successor element of the given input."""

        key_node = self.lookup(data)

        if key_node.right:
            return self.min(key_node.right)
        else:
            parent_node = key_node.parent

            while parent_node is not None and parent_node.right == key_node:
                key_node = parent_node
                parent_node = key_node.parent

        return parent_node.data

    def predecessor(self, data):

        """Returns the predecessor of the given input."""

        key_node = self.lookup(data)

        if key_node.left:
            return self.max(key_node.left)
        else:
            parent_node = key_node.parent

            while parent_node != None and parent_node.left == key_node:
                key_node = parent_node
                parent_node = key_node.parent

        return parent_node.data

    def transplant(self, x, y):

        """Replaces X with Y node."""

        y.parent = x.parent

        if not x.parent:
            self.root = y
        else:
            if x.parent.left == x:
                x.parent.left = y
            else:
                x.parent.right = y

    def inOrder(self, root):

        """Travers the tree in-order and returns the elements."""

        res = []

        if root:
            res = self.inOrder(root.left)
            res.append(root.data)
            res += self.inOrder(root.right)

        return res

    def preOrder(self, root):

        """Travers the tree pre-order and returns the elements."""

        res = []

        if root:
            res.append(root.data)
            res += self.preOrder(root.left)
            res += self.preOrder(root.right)

        return res

    def postOrder(self, root):

        """Travers the tree post-order and returns the elements."""

        res = []

        if root:
            res += self.postOrder(root.left)
            res += self.postOrder(root.right)
            res.append(root.data)

        return res

    def delete(self, data):

        """Deletes the given element from the tree in O(logN)."""

        rem = self.lookup(data)

        if rem.left is None:
            self.transplant(rem, rem.right)
        elif rem.right is None:
            self.transplant(rem, rem.left)
        else:
            y = self.min(rem.right)

            if y.right:
                self.transplant(y, y.right)
                y.right = rem.right
                y.right.parent = y

            self.transplant(rem, y)
            y.left = rem.left
            y.left.parent = y

        self.rebalance(rem.parent)

    def height(self, node):

        """Returns the height of the node."""

        if node is None:
            return -1

        return node.height

    def update_height(self, node):

        """Updates the node with new heights."""

        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def rotateRight(self, x):

        """Performs right rotation of the given node."""

        y = x.left
        self.transplant(x, y)

        x.left = y.right
        if x.left:
            x.left.parent = x

        y.right = x
        y.right.parent = y

        self.update_height(x)
        self.update_height(y)

    def rotateLeft(self, x):

        """Performs left rotation of the given node."""

        y = x.right
        self.transplant(x, y)

        x.right = y.left

        if x.right:
            x.right.parent = x

        y.left = x
        y.left.parent = y

        self.update_height(x)
        self.update_height(y)

    def rebalance(self, x):

        """Rebalance the tree after deleting / inserting new nodes."""

        while x is not None:

            self.update_height(x)

            if self.height(x.left) > 1 + self.height(x.right):
                if self.height(x.left.left) >= self.height(x.left.right):
                    self.rotateRight(x)
                else:
                    self.rotateLeft(x.left)
                    self.rotateRight(x)
            elif self.height(x.right) > 1 + self.height(x.left):
                if self.height(x.right.right) >= self.height(x.right.left):
                    self.rotateLeft(x)
                else:
                    self.rotateRight(x.right)
                    self.rotateLeft(x)

            x = x.parent