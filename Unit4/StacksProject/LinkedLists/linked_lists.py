"""
linked_lists.py
Contains the LinkedList ADT
"""
from .node import Node


class LinkedList:
    """
    A linked list structure, where each Node points to the
    next Node in the list.
    """

    def __init__(self):
        """
        Constructor for LinkedList ADT
        """
        self.head = None

    def insert(self, data):
        """
        Inserts data at the beginning of the list

        Paramaters:
        -----------
        data : String
            The data being added to the list
        """
        node = Node(data)
        node.set_next(self.head)
        self.head = node

    def remove(self, data):
        """
        Removes the first instance of a data

        Paramaters:
        -----------
        data : String
            The data being removed by the list
        """
        previous_node = None
        current_node = self.head

        while current_node.get_next() is not None:
            if current_node.get_data() == data:
                if previous_node is None:
                    # If the current node is the head
                    self.head = current_node.get_next()
                else:
                    # If the current node is in the middle
                    # Point the previous node to the node after the current node
                    previous_node.set_next(current_node.get_next())
                break
            previous_node = current_node
            current_node = current_node.get_next()

    def pop(self):
        """
        Removes and returns the first element in the list

        Returns:
        --------
        String
            The first element in the list
        """
        temp_node = self.head
        self.head = self.head.get_next()
        return temp_node.get_data()

    def peek(self):
        """
        Returns the first element in the list

        Returns:
        --------
        String
            The first element in the list
        """
        return self.head.get_data()

    def __iter__(self):
        """
        Initializes iteration

        Returns:
        --------
        _LinkedListIterativeHelper
            An ADT that enables iteration through LinkedList
        """
        return _LinkedListIterativeHelper(self)


class _LinkedListIterativeHelper:
    """
    Allows for iteration through the LinkedList ADT
    """

    def __init__(self, linked_list):
        """
        Constructor for the _LinkedListIterativeHelper ADT

        Paramaters:
        -----------
        linked_list : LinkedList
            The LinkedList being iterated through
        """
        self._head = linked_list.head
        self._current_node = None
        self._next_node = self._head

    def __iter__(self):
        """
        Initializes the iteration
        """
        self._current_node = None
        self._next_node = self._head

    def __next__(self):
        """
        Returns the next value in each iteration
        """
        if self._next_node is None:
            raise StopIteration

        self._current_node = self._next_node
        self._next_node = self._next_node.get_next()

        return self._current_node.get_data()
