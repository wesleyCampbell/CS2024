"""
main.py
The driver file for the BSTs Project

Description:
    Takes in a text file and, using a tree, counts the number
    each letter appears in the file.
"""

import random

from pair import Pair
from bst import Node
from bst import BST
import os

DATA_FILE = os.path.join(os.getcwd(), "around-the-world-in-80-days-3.txt")
VALID_LETTERS = "abcdefghijklmnopqrstuvwxyz0123456789"


def make_tree():
    """
    Makes a tree containing the counts of the letters in the input file

    :returns (BST): The tree
    """
    letter_tree = BST()

    with open(DATA_FILE, 'r') as data_file:
        for char in data_file.read():
            char_ordinal = ord(char)
            if char.lower() in VALID_LETTERS:
                # If the character is already in letter_tree, increase the count
                # else, insert the character in letter_tree
                try:
                    letter = letter_tree.find(char)
                    letter.count += 1
                except ValueError:
                    letter_tree.add(Pair(char))

    # letter_tree = letter_tree.rebalance()
    return letter_tree


def make_test_tree(n=10):
    data = Pair(random.randint(0, 1000))
    root = Node(data)

    tree = BST(root)

    for i in range(n):
        tree.add(Node(Pair(random.randint(0, 10000))))

    print("root: " + str(tree.root))
    print(tree)

    print(tree.height())


def analyze_txt():
    letters = set()
    with open(DATA_FILE, 'r') as f:
        for char in f.read():
            if char not in VALID_LETTERS and char not in VALID_LETTERS.upper():
                letters.add(char)

    for x in letters:
        print(x)


def main():
    """
    Main function where program kicks off
    """
    tree = make_tree()
    print(f"root: {tree.root}")
    for pair in tree.inorder():
        print(pair)


if __name__ == "__main__":
    main()
