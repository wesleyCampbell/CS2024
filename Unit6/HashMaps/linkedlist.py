"""
linkedlist.py
Contains the LinkedList ADT for the project
"""


class LinkedList:
    """
    A linked list for storing values

    Attributes:
    -----------

    Methods:
    --------
    add(data): Add a tuple to the linked list
    remove(data): Remove a tuple from the linked list
    is_empty(): Returns true if there are no items in the list
    find(data): Return the index of data in the linked list
    get(index): Return the data at index
    """

    def __init__(self):
        """
        Constructor for the LinkedList
        """
        self.head = None

    def add(self, data):
        """
        Add a data into the linked list at head position

        Paramaters:
        data : tuple
            The data to be added
        """
        temp_node = self.head
        self.head = Node(data)
        self.head.set_next(temp_node)

    def remove(self, data):
        current_node = self.head
        previous_node = None

        # If the list is empty
        if current_node is None:
            raise ValueError("data is not in LinkedList")

        # Iterate through all but the last Node
        while current_node.get_next() is not None:
            # If the current node's data is to be removed
            if current_node.get_data() == data:
                # If the node is the head
                if previous_node is None:
                    # Set the next value as the head
                    self.head = current_node.get_next()
                else:
                    previous_node.set_next(current_node.get_next())

            previous_node = current_node
            current_node = current_node.get_next()

        # If the last node's data is to be removed
        if current_node.get_data() == data:
            # If the node is the head
            if previous_node is None:
                # Set the next value as the head
                self.head = current_node.get_next()
            else:
                previous_node.set_next(current_node.get_next())

        raise ValueError("data is not in LinkedList")

    def find(self, data):
        """
        Returns the index of data if it is in LinkedList

        Returns:
        --------
        int
            The index of data
        """
        index = 0
        current_node = self.head

        while current_node.get_next() is not None:
            if current_node.get_data() == data:
                return index

            current_node = current_node.get_next()
            index += 1

        if current_node.get_data() == data:
            return index

        raise ValueError("data is not in LinkedList")

    def get(self, index):
        current_node = self.head

        for _ in range(index):
            try:
                current_node = current_node.get_next()
            except AttributeError:
                raise IndexError(f"There are not {index} values in LinkedList")

        return current_node.get_data()

    def is_empty(self):
        """
        Returns True if the list is emtpy
        """
        return self.head is None


class Node:
    """
    A Node ADT used for storing data in the LinkedList ADT

    Methods:
    --------
    get_data(): Return the data of the Node
    set_data(data): Set the data of the Node
    get_next(): Get the next Node
    set_next(node): Set the next Node
    """

    def __init__(self, data):
        """
        Constructor for Node 
        """
        self._data = data
        self._next = None

    def get_data(self):
        """
        Return the data of the Node
        """
        return self._data

    def set_data(self, data):
        """
        Set the data of the Node

        Paramaters:
        -----------
        data : tuple
            The data to set the Node
        """
        self._data = data

    def get_next(self):
        """
        Return the next Node
        """
        return self._next

    def set_next(self, node):
        """
        Set the next Node

        Paramaters:
        -----------
        node : Node
            The next Node
        """
        self._next = node
