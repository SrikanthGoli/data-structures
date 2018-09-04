# Implementing Binary Search Tree data structure
class Node(object):

    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class binarySearchTree(object):

    def __init__(self, data=None):

        """Performs insert, delete, search in O(logH)."""

        self.root = Node(data)

    def push(self, data):

        """Inserts new node in O(logH) time."""

        prev_node = None
        new_node = Node(data)
        curr_node = self.root

        if curr_node.data is None:
            self.root = new_node

        else:
            while curr_node is not None:
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

    def lookup(self, data):

        """Returns the Node of the given input."""

        curr = self.root

        while curr is not None:

            if data < curr.data:
                curr = curr.left
            elif data > curr.data:
                curr = curr.right
            elif data == curr.data:
                return curr

        return False

    def min(self, root):

        """Returns the min element from the given root."""

        curr = root

        while curr:
            res = curr
            curr = curr.left

        return res.data

    def max(self, root):

        """Returns the max element from the given root."""

        curr = root

        while curr:
            res = curr
            curr = curr.right

        return res.data

    def inorder_traversal(self, root):

        """Travers the tree in-order and returns the elements."""

        res = []

        if root is not None:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res += self.inorderTraversal(root.right)

        return res

    def preorder_traversal(self, root):

        """Travers the tree pre-order and returns the elements."""

        res = []

        if root:
            res.append(root.data)
            res += self.preorderTraversal(root.left)
            res += self.preorderTraversal(root.right)

        return res

    def postorder_traversal(self, root):

        """Travers the tree post-order and returns the elements."""

        res = []

        if root:
            res += self.postorderTraversal(root.left)
            res += self.postorderTraversal(root.right)
            res.append(root.data)

        return res

    def successor(self, data):

        """Returns the successor element of the given input."""

        curr = self.root

        while curr.data != data:
            if data < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        if curr.right:
            return self.min(curr.right)

        parent = curr.parent

        while parent is not None and parent.right.data == curr.data:
            curr = parent
            parent = curr.parent

        return parent.data

    def predecessor(self, data):

        """Returns the predecessor of the given input."""

        curr = self.root

        while curr.data != data:
            if data < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        if curr.left:
            return self.max(curr.left)

        parent = curr.parent

        while parent is not None and parent.left.data == curr.data:
            curr = parent
            parent = curr.parent

        return parent.data

    def transplant(self, parent, child):

        """Replaces parent with child node."""

        p = self.lookup(parent)
        c = self.lookup(child)

        if p.parent == None:
            self.root = c
        elif p.parent.left.data == p.data:
            p.parent.left = c
        elif p.parent.right.data == p.data:
            p.parent.right = c

        if c.data:
            c.parent == p.parent

    def delete(self, data):

        """Deletes the given element from the tree in O(logN)."""

        rem = self.lookup(data)

        if rem.left is None:
            self.transplant(data, rem.right.data)
        elif rem.right is None:
            self.transplant(data, rem.left.data)
        else:
            successor = self.min(rem.right)
            y = self.lookup(successor)

            if y.parent.data != data:
                self.transplant(y.data, y.right.data)
                rem.right = rem.right
                y.right.parent = y

            self.transplant(rem.data, y.data)
            y.left = rem.left
            y.left.parent = y