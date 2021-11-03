"""
node.py
Contains the Node ADT
"""


class Node:
    """
    Each Node is an item in the LinkedLists ADT.
    """

    def __init__(self, data):
        """
        Constructor for Node ADT

        Paramaters:
        -----------
        data : String
            The data the node contains
        """
        self.data = data
        self.next = None

    def set_next(self, node):
        """
        Points the next pointer to a Node

        Paramaters:
        -----------
        node : Node
            The node to be pointed to
        """
        self.next = node

    def get_next(self):
        """
        Returns the next Node
        """
        return self.next

    def get_data(self):
        """
        Returns the datad
        """
        return self.data
