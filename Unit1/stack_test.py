"""
A example of an Abstract Data Type (ADT).
"""


class Stack:
    """
    A class that functions as a Stack ADT

    Attributes
    ----------
    items : list
        The list of items on the stack

    Methods
    -------
    push(item):
        Adds item to the top of the stack
    pop():
        Removes and returns the top item of the stack
    peek():
        Returns the top item of the stack
    is_empty():
        Returns True if the stack is empty and False if otherwise
    size():
        Returns the number of items in the stack
    """
    def __init__(self):
        """
        Constructs the attributes for the Stack class
        """
        self.items = []

    def push(self, item):
        """
        Adds item to the top of the stack

        Parameters
        ----------
        item (Object): The item being added to the top of the stack

        Returns
        -------
        None
        """
        self.items = [item] + self.items

    def pop(self):
        """
        Removes and returns the top item of the stack

        Returns
        -------
        items[0] (Object): The item on the top of the stack
        """
        return self.items.pop(0)

    def peek(self):
        """
        Gets the top item of the stack

        Returns
        items[0] (Object): The item on the top of the stack
        -------

        """
        return self.items[0]

    def is_empty(self):
        """
        If the stack is empty, return True. Return False otherwise.

        Returns
        -------
        (Boolean): Is the stack empty?
        """
        return self.size() == 0

    def size(self):
        """
        Gets the number of items on the stack

        Returns
        -------
        return len(items) (int): The size of the stack
        """
        return len(self.items)


def main():
    """
    The main() function of the stack_test.py file.
    Tests out my new docstring format.

    Returns
    -------
    None
    """
    stack = Stack()

    print(help(stack))


def test_stack():
    """
    A pytest test for the Stack class.
    This test function tests every attribute of the Stack class.

    Returns
    -------
    None
    """
    stack = Stack()

    assert stack.size() == 0
    assert stack.is_empty()

    for i in range(10):
        stack.push(i)

    assert stack.size() == 10
    assert stack.pop() == 9
    assert stack.size() == 9
    assert stack.peek() == 8


if __name__ == "__main__":
    main()
