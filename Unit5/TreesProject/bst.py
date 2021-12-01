"""
bst.py
Contains the Binary Search BST (BST) ADT
"""
from pair import Pair


class Node:
    """
    A Node class used in the BST.
    It contains data and points to the left and right nodes
    """

    def __init__(self, data):
        """
        Constructor function for Node class

        Paramaters:
        -----------
        data : Pair || Node
            The data
        """
        # If data is already a Node
        if isinstance(data, Node):
            self.data = data.get_data()
        elif isinstance(data, Pair):
            self.data = data
        else:
            raise TypeError("data paramater must be Pair or Node")

    def get_data(self):
        """
        Gets the node's data

        Returns:
        --------
        Pair: the data pair
        """
        return self.data

    def set_data(self, new_data):
        """
        Sets the node's data

        Paramaters:
        -----------
        new_data : Pair
            The new data for the node

        :return: None
        """
        self.data = new_data

    def __str__(self):
        return self.data.__str__()


class BST:
    """
    A Binary Search BST
    Manages, sorts, and rebalances Nodes
    """

    def __init__(self, root_node=None):
        """
        Constructor function

        Paramaters:
        -----------
        root_node : Node || Pair
            The root node for the tree
        """
        if isinstance(root_node, Node) or root_node is None:
            self.root = root_node
        elif isinstance(root_node, Pair):
            self.root = Node(root_node)
        else:
            raise ValueError("root_node must be of type Node or Pair")

        self.left_tree = None
        self.right_tree = None

    def add(self, data_node):
        """
        Inserts a data into its sorted position

        Paramaters:
        -----------
        data_node: the data

        :return: BST
        """
        data_node = Node(data_node)
        if self.root is None:
            # If the tree has no Root value
            self.root = data_node
        elif data_node.get_data() <= self.root.get_data():
            # If the data is less than the root, put it in the left tree
            if self.left_tree is not None:
                # If there is a left subtree, hand the data off to it
                self.left_tree.add(data_node)
            else:
                # If there is no left subtree, create a new subtree using data
                self.left_tree = BST(data_node)
        else:
            # If the data is greater than the root, put it in the right tree
            if self.right_tree is not None:
                # If the right subtree exists, hand the data over to it
                self.right_tree.add(data_node)
            else:
                # If the right subtree does not exist, create a new BST
                self.right_tree = BST(data_node)

        return self

    def find(self, data):
        """
        Finds a data element in the tree

        :param data: (Int) The data being looked for

        :return: Pair
        """
        if self.root is None:
            raise ValueError
        if self.root.get_data().letter == data:
            return self.root.get_data()
        if self.left_tree is None and self.right_tree is None:
            raise ValueError
        if self.left_tree is not None and data < self.root.get_data().letter:
            return self.left_tree.find(data)
        if self.right_tree is not None and data >= self.root.get_data().letter:
            return self.right_tree.find(data)
        raise ValueError

    def remove(self, data):
        """
        Remove the first instance of data in the tree

        Paramaters:
        -----------
        data : Pair
            The data to be removed

        Returns:
        --------
        self : BST
            Returns the modified tree
        """
        return self._remove(data)

    def _remove(self, data, parent=None, direction=None):
        """
        Helper function for self.remove(data).
        Exists so that parent and direction are not messed with

        Paramaters:
        -----------
        data : Pair
            The data to be removed
        parent : Node
            The parent of the current Node
        direction : String ('left' || 'right')
            Is the current Node a left or right child of its parent?

        Returns:
        --------
        self : BST
            Returns the modified tree
        """
        if self.root.get_data() == data:
            # If the root Node matches the data value
            if self.left_tree is None and self.right_tree is None:
                # If the Node has no children; it is a leaf Node
                if parent is None:
                    # If the node is the very first node
                    self.root = None
                else:
                    # If the node is a leaf
                    if direction == "left":
                        # If the Node is a left child of its parent
                        parent.left_tree = None
                    if direction == "right":
                        # If the Node is a right child of its parent
                        parent.right_tree = None

            elif self.left_tree is not None and self.right_tree is not None:
                # If the Node has 2 children
                if direction == "right" or parent is None:
                    # If the Node is a right child, take the futhest left Node
                    # of the right subtree and replace the current Node
                    # Same principle applies to the root Node
                    current_tree = self.right_tree
                    previous_tree = self
                    while current_tree.left_tree is not None:
                        previous_tree = current_tree
                        current_tree = current_tree.left_tree

                    self.root.set_data(current_tree.root.get_data())
                    previous_tree.set_left_tree(None)

                elif direction == "left":
                    # If the Node is a left child, take the furthest right Node
                    # of the left subtree and replace the current Node
                    current_tree = self.left_tree
                    previous_tree = self
                    while current_tree.right_tree is not None:
                        previous_tree = current_tree
                        current_tree = current_tree.right_tree

                    # Replace the current Node with the leaf Node and delete the leaf Node
                    self.root.set_data(current_tree.root.get_data())
                    previous_tree.set_right_tree(None)
            else:
                # The current Node has only one child
                if self.left_tree is not None:
                    # If the left tree exists
                    if direction == "right":
                        # If the current Node is a right child
                        parent.set_right_tree(self.left_tree)
                    elif direction == "left":
                        # If the current Node is a left child
                        parent.set_left_tree(self.left_tree)
                elif self.right_tree is not None:
                    # If the right tree exists
                    if direction == "right":
                        # If the current Node is a right child
                        parent.set_right_tree(self.right_tree)
                    elif direction == "left":
                        # If the current Node is a left child
                        parent.set_left_tree(self.right_tree)

        elif data.letter < self.root.get_data().letter:
            # If the data is less than the current Node search the left subtree
            self.left_tree._remove(data, self, "left")

        elif data.letter > self.root.get_data().letter:
            # If the data is greater than the current Node search the right subtree
            self.right_tree._remove(data, self, "right")

        return self

    def set_left_tree(self, tree):
        """
        Sets the tree's left tree

        Paramaters:
        -----------
        tree : BST
            The subtree
        """
        self.left_tree = tree

    def set_right_tree(self, tree):
        """
        Sets the tree's right tree

        Paramaters:
        -----------
        tree : BST
            The subtree
        """
        self.right_tree = tree

    @staticmethod
    def _balance(nodes):
        """
        Balances the tree by taking all the nodes,
        taking the median for the new root node

        Paramaters:
        -----------
        nodes : List<Node>
            The list of Nodes

        :return: (BST) self
        """

        # Create a new tree with the median node as the root
        if len(nodes) == 0:
            return BST()

        pivot = len(nodes) // 2
        new_tree = BST(nodes[pivot])

        left_tree = None
        right_tree = None

        # Create a balanced tree with the lesser nodes
        left_tree = BST._balance(nodes[:pivot])
        # Create a balanced tree with the greater nodes
        right_tree = BST._balance(nodes[pivot+1:])

        new_tree.set_left_tree(left_tree)
        new_tree.set_right_tree(right_tree)

        return new_tree

    def rebalance(self):
        """
        Rebalances the tree

        :return: BSTs
        """
        nodes = self.inorder()
        bst = BST._balance(nodes)

        # Clear the tree and set self to bst
        self.clear_tree()
        self.copy(bst)

        return self

    def copy(self, tree):
        """
        Copies another tree and puts its data into self

        Paramaters:
        -----------
        tree : BST
            The tree we are copying
        """
        self.root = tree.root
        self.left_tree = tree.left_tree
        self.right_tree = tree.right_tree

    def clear_tree(self):
        """
        Deletes the entire tree, leaving behind an empty tree
        """
        self.root = None
        self.left_tree = None
        self.right_tree = None

    def inorder(self):
        """
        Traverses the list in order:
        inorder(leftTree)
        root
        inorder(rightTree)

        :return: List<Pair>
        """
        left = right = []

        if self.root is None:
            return []

        if self.left_tree is not None:
            left = self.left_tree.inorder()
        root = [self.root.get_data()]
        if self.right_tree is not None:
            right = self.right_tree.inorder()

        return left + root + right

    def preorder(self):
        """
        Returns a list of the tree in preorder form

        :return: List<Pair>
        """
        if self.root is None:
            return []

        root = [self.root.get_data()]
        left_tree = []
        right_tree = []

        if self.left_tree is not None:
            left_tree = self.left_tree.preorder()
        if self.right_tree is not None:
            right_tree = self.right_tree.preorder()

        return root + left_tree + right_tree

    def postorder(self):
        """
        Returns a list of the tree's Nodes in postorder

        :return: List<Pair>
        """
        if self.root is None:
            return []

        root = [self.root.get_data()]
        left_tree = []
        right_tree = []

        if self.left_tree is not None:
            left_tree = self.left_tree.postorder()
        if self.right_tree is not None:
            right_tree = self.right_tree.postorder()

        return left_tree + right_tree + root

    def is_empty(self):
        """
        Tests to see whether the tree is emtpy

        :return: Boolean
        """
        return self.size() == 0

    def size(self):
        """
        Returns how many Nodes the tree has

        :return: Int
        """
        return len(self.inorder())

    def height(self):
        """
        Gets the height of the tree

        :return: Int
        """
        return self._height(self)

    def _height(self, tree):
        if tree is None:
            return 0
        return max(self._height(tree.left_tree), self._height(tree.right_tree)) + 1

    def __str__(self):
        return f"root: {self.root}\n left: {self.left_tree.__str__()}\
         right: {self.right_tree.__str__()}"
