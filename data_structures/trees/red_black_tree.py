# Red black tree data structure

class Nil(object):

    def __init__(self):

        self.color = "Black"

class Node(object):

    def __init__(self, data = None):

        self.data = data
        self.color = "Red"
        self.parent = None
        self.left = None
        self.right = None

class Red_Black_Tree(object):

    """Red black tree: Provides insertion,
    search, and deletion in O(logN) time.
    """

    def __init__(self, data):

        self.Nil = Nil()
        self.root = Node(data)
        self.root.color = "Black"
        self.root.parent = self.Nil
        self.root.left = self.Nil
        self.root.right = self.Nil

    def insert(self, data):

        """Inserts an element in Red black tree
        in O(logN)."""

        curr_node = self.root
        prev_node = self.Nil
        null = self.Nil
        new_node = Node(data)

        while curr_node is not null:
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

        new_node.left = self.Nil
        new_node.right = self.Nil

        self.insert_fixup(new_node)

    def insert_fixup(self, x):

        """Fixes the violation caused by the new node"""

        while x.parent.color == "Red":
            if x.parent.parent.left == x.parent:
                y = x.parent.parent.right
                if y.color == "Red":
                    x.parent.color = "Black"
                    y.color = "Black"
                    x.parent.parent.color = "Red"
                    x = x.parent.parent
                else:
                    if x == x.parent.right:
                        x = x.parent
                        self.left_rotate(x)
                    x.parent.color = "Black"
                    x.parent.parent.color = "Red"
                    self.right_rotate(x.parent.parent)
            else:
                if x.parent.parent.right == x.parent:
                    y = x.parent.parent.left
                    if y.color == "Red":
                        x.parent.color = "Black"
                        y.color = "Black"
                        x.parent.parent.color = "Red"
                        x = x.parent.parent
                    else:
                        if x == x.parent.left:
                            x = x.parent
                            self.right_rotate(x)
                        x.parent.color = "Black"
                        x.parent.parent.color = "Red"
                        self.left_rotate(x.parent.parent)

        self.root.color = "Black"


    def transplant(self, x, y):

        """Replace x with y node"""

        y.parent = x.parent

        if x.parent is self.Nil:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y

    def right_rotate(self, x):

        """Performs right rotation of nodes."""

        y = x.left
        self.transplant(x, y)

        x.left = y.right

        if x.left:
            x.left.parent = x

        y.right = x
        y.right.parent = y

    def left_rotate(self, x):

        """Performs left rotation of nodes."""

        y = x.right
        self.transplant(x, y)

        x.right = y.left
        if x.right:
            x.right.parent = x

        y.left = x
        y.left.parent = y

    def lookup(self, data):

        """Looks up the respective node for a given
        data point in the tree
        """

        curr_node = self.root

        while curr_node.data is not data:
            if data < curr_node.data:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        return curr_node

    def min(self, x):

        """Returns the min node in the tree"""

        curr_node = x

        while curr_node is not self.Nil:
            curr_node = curr_node.left

        return curr_node.parent

    def max(self, x):

        """Returns the max node in the tree"""

        curr_node = x

        while curr_node is not self.Nil:
            curr_node = curr_node.right

        return curr_node.parent

    def delete(self, data):

        """Deletes a given data point in the tree."""

        rem = self.lookup(data)
        y = rem
        y_original_color = y.color

        if rem.left is self.Nil:
            x = rem.right
            self.transplant(rem, rem.right)
        elif rem.right is self.Nil:
            x = rem.left
            self.transplant(rem, rem.left)
        else:
            y = self.min(rem.right)
            y_original_color = y.color
            x = y.right
            if y.parent is rem:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = rem.right
                y.right.parent = y

            self.transplant(rem, y)
            y.left = rem.left
            y.left.parent = y
            y.color = rem.color

        if y_original_color is "Black":
            self.delete_fixup(x)

    def delete_fixup(self, x):

        """Fixes the violations caused by the deleted node"""
        
        while x is not self.root and x.color == "Black":
            if x.parent.left is x:
                w = x.parent.right
                if w.color == "Red":
                    w.color = "Black"
                    x.parent.color = "Black"
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if x.left.color == "Black" and x.right.color == "Black":
                    w.color = "Red"
                    x = x.parent
                else:
                    if w.right.color == "Black":
                        w.left.color = "Black"
                        w.color = "Red"
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "Black"
                    w.right.color = "Black"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "Red":
                    w.color = "Black"
                    x.parent.color = "Black"
                    self.right_rotate(x.parent)
                    w = x.parent.right
                if x.left.color == "Black" and x.right.color == "Black":
                    w.color = "Red"
                    x = x.parent
                else:
                    if w.left.color == "Black":
                        w.right.color = "Black"
                        w.color = "Red"
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "Black"
                    w.right.color = "Black"
                    self.right_rotate(x.parent)
                    x = self.root

        x.color = "Black"

    def inorder_traversal(self, root):

        """Performs inorder traversal of the tree"""

        res = []

        if root is not self.Nil:
            res = self.inorder_traversal(root.left)
            res.append(root.data)
            res += self.inorder_traversal(root.right)

        return res

    def preorder_traversal(self, root):

        """Performs preorder traversal of the tree"""

        res = []

        if root is not self.Nil:
            res.append(root.data)
            res += self.preorder_traversal(root.left)
            res += self.preorder_traversal(root.right)

        return res

    def postorder_traversal(self, root):

        """Performs postorder traversal of the tree"""

        res = []

        if root is not self.Nil:
            res += self.postorder_traversal(root.left)
            res += self.postorder_traversal(root.right)
            res.append(root.data)

        return res
