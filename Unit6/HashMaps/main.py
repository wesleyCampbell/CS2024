"""
main.py
Main file for the HashMap project
"""
import sys

WEIGHT = 200.00

weight_calls = 0


def weight_on(row, column):
    """
    Finds the weight a given person in a people pyramid is experiencing

    Paramaters:
    -----------
    row : int
        The row of the person
    column : int
        The column of the person

    Returns:
    --------
    The weight : float
    """
    # Return the total weight of a person minus his personal w
    return weight(row, column) - WEIGHT


def weight(row, column):
    """
    A recursive function that returns the weight of person in a pyramid

    Paramaters:
    -----------
    row : int
        The row of the person
    column : int
        The column of the person

    Returns:
    The weight : float
    """
    # If the person is on the top
    weight_calls += 1

    # Base case
    if (row, column) == (0, 0):
        return WEIGHT

    # If there is no one on the left
    if column - 1 < 0:
        return WEIGHT + weight(row - 1, column) / 2
    # If there is no one on the right
    elif column > row - 1:
        return WEIGHT + weight(row - 1, column - 1) / 2
    # If the person is internal
    return WEIGHT + weight(row - 1, column - 1) / 2 + weight(row - 1, column) / 2


def main():
    """
    The driver function
    """
    row_num = sys.argv[1]
    for row in range(int(row_num)):
        line = ''
        for col in range(row + 1):
            line += str(weight_on(row, col)) + " "
        print(line)

    print("\n")
    print(f"Function calls: {weight_calls}")


if __name__ == "__main__":
    main()
