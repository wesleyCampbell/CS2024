"""
main.py
Main file for the HashMap project
"""
import sys
import time
from hashmap import HashMap

WEIGHT = 200.00
cache = HashMap()


class Counter:
    def __init__(self):
        self.count = 0

    def get_count(self):
        return self.count

    def increment(self):
        self.count += 1


function_counter = Counter()
cache_counter = Counter()


def weight_on(row, column):
    """
    Finds the weight a given person in a people pyramid is experiencing

    Paramaters:
    -----------
    row : int
        The row of the person
    column : int
        The column of the person
    counter : Counter
        Used for tracking number of weight() calls

    Returns:
    --------
    The weight : float
    """
    # Return the total weight of a person minus his personal weight
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

    counter : Counter
        Tracks the total number of function calls

    Returns:
    The weight : float
    """
    # Increment counter, if applicable
    function_counter.increment()
    output = 0
    try:
        output = cache.get((row, column))
        cache_counter.increment()
    except KeyError:
        # If the person is on the top
        # Base case
        if (row, column) == (0, 0):
            output = WEIGHT
        # If there is no one on the left
        elif column - 1 < 0:
            output = WEIGHT + weight(row - 1, column) / 2
        # If there is no one on the right
        elif column > row - 1:
            output = WEIGHT + weight(row - 1, column - 1) / 2
        # If the person is internal
        else:
            output = WEIGHT + weight(row - 1, column - 1) / \
                2 + weight(row - 1, column) / 2

        cache.set((row, column), output)
    return output


def print_pyramid(row_num):
    """
    Prints the wieghts each person in a pyramid experiances

    Paramaters:
    -----------
    row_num : int
        The number of rows in the pyramid
    counter : Counter
        Used for tracking the number of calls of weight()

    Returns:
    --------
    The text of the pyramid : str
    """
    output = ""
    for row in range(int(row_num)):
        line = ''
        for col in range(row + 1):
            line += "{:0.2f} ".format(weight_on(row, col))
        # print(line)
        output += line + "\n"

    return output


def main(row_num):
    """
    The driver function
    Prints to the console and outputs to a file the pyramid

    Paramaters:
    -----------
    row_num : int
        The number of rows in the pyramid
    """
    # Time the function
    begin = time.perf_counter()
    pyramid = print_pyramid(row_num)

    # Calculate stats
    elapsed_time = time.perf_counter() - begin
    function_calls = function_counter.get_count()
    cache_hits = cache_counter.get_count()

    # Append stats to output
    pyramid += f"\nElapsed Time: {elapsed_time} seconds"
    pyramid += f"\nNumber of Function Calls: {function_calls}"
    pyramid += f"\nNumber of Cache Hits: {cache_hits}"

    print("="*24 + "\n" + pyramid)

    # Push the function output to the file
    # with open("part2.txt", "w") as output:
    #     output.write(pyramid)


if __name__ == "__main__":
    rows = sys.argv[1]
    main(rows)
