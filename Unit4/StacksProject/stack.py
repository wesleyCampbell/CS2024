"""
Stack.py
Contains the Stack ADT
"""

from LinkedLists.linked_lists import LinkedList


class Stack:
    """
    A linear structure.
    Implements a first in first out structure
    """

    def __init__(self):
        """
        Constructor for the Stack ADT
        """
        self.items = LinkedList()
        self.size = 0

    def push(self, item):
        """
        Inserts an item onto the top of the stack

        Paramaters:
        -----------
        item : String
            The item being put on the stack

        Returns:
        --------
        None
        """
        self.items.insert(item)
        self.size += 1

    def pop(self):
        """
        Removes and returns the top item on the stack

        Returns:
        --------
        Object
            The top item on the stack
        """
        self.size -= 1
        return self.items.pop()

    def top(self):
        """
        Returns the top item on the stack

        Returns:
        --------
        Object
            The top item on the stack
        """
        return self.items.peek()

    def size(self):
        """
        Returns the how many items are on the stack

        Returns:
        --------
        Int
            How many items are on the stack
        """
        return self.size

    def is_empty(self):
        """
        Determins whether the stack is empty

        Returns:
        --------
        Boolean
            Is the stack empty?
        """
        return self.size == 0

    def clear(self):
        """
        Removes all items on the stack

        Returns:
        --------
        Stack
            Returns itself
        """
        for i in self.items:
            self.items.remove(i)
        return self
