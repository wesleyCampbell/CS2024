"""
pair.py
The file for the Pair ADT
"""


class Pair:
    """
    Encapsulates a letter and a count into a single instance
    """

    def __init__(self, letter, count=1):
        """
        Constructor function

        :param letter: The letter
        :param count: The number of letter
        """
        self.letter = letter
        self.count = count

    def __eq__(self, other):
        """
        Checks if two Pair instances are equal
        """
        return ord(self.letter) == ord(other.letter)

    def __ne__(self, other):
        """
        Checks if two Pair instances are not equal
        """
        return ord(self.letter) != ord(other.letter)

    def __lt__(self, other):
        """
        Checks if self is less than another Pair
        """
        return ord(self.letter) < ord(other.letter)

    def __le__(self, other):
        """
        Checks if self is less than or equal to another Pair
        """
        return ord(self.letter) <= ord(other.letter)

    def __gt__(self, other):
        """
        Checks if self is greater than another Pair
        """
        return ord(self.letter) > ord(other.letter)

    def __ge__(self, other):
        """
        Checks if self is greater than or equal to another Pair
        """
        return ord(self.letter) >= ord(other.letter)

    def __repr__(self):
        """
        Return a string of self
        """
        return f"({self.letter}, {self.count})"

    def __str__(self):
        """
        Return a string of self
        """
        return f"({self.letter}, {self.count})"
