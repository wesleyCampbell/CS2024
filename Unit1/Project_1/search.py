"""
Contains three different searching algorithms:
  - A linear search algorithm
  - A binary search algorithm (Recursive)
  - A jump search algorithm (Recursive)
Compares the time it takes to run each algorithm.
"""
import time


def time_it(func):
    """
    Prints out to the console how much time a function
    takes to run
    Parameters
    ----------
    func : Function
        The function to time

    Returns
    -------
    wrap : Function
        The wrapper function
    """

    def wrap(*args, **kwargs):
        """
        This function is a wrapper function for func.
        It times how much time func takes to operate.
        Parameters
        ----------
        args: The arguments for func
        kwargs: The key-word arguments for func

        Returns
        -------
        Object: The return value of func()
        """
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"{func.__name__} took {round((end-start) * 1000)} milliseconds")
        return result

    return wrap


def make_data(length):
    """
    Makes a sorted list of values
    Parameters
    ----------
    length (int): The number of values to be in the list

    Returns
    -------
    (list): The sorted data list
    """
    return list(range(length))


def test_binary_search():
    """
    Tests the binary_search algorithm.
    Used for debugging.
    Returns
    -------
    None
    """
    lyst = make_data(30)

    for i in range(30):
        assert binary_search(lyst, i)

    assert not binary_search(lyst, 34)
    assert not binary_search(lyst, 100)


def test_jump_search():
    """
    Tests the jump_search algorithm.
    Used for debugging.
    Returns
    -------
    None
    """
    lyst = make_data(90)
    for i in range(90):
        assert jump_search(lyst, i)

    assert not jump_search(lyst, 100)
    assert not jump_search(lyst, -1)


@time_it
def linear_search(lyst, target):
    """
    Performs a linear search for target in a given list.

    Parameters
    ----------
    lyst : list
        A sorted list
    target : int
        The target of the search

    Returns
    -------
    (Boolean): Is target in lyst?
    """

    for i in lyst:
        if i == target:
            return True
        elif i > target:
            return False
        i += 1
    return False


def _binary_search(lyst, target):
    """
    Performs a binary search on a list.
    This function is recursive.

    Parameters
    ----------
    lyst : List
        The list being searched
    target : int
        The item we are searching for in the list

    Returns
    -------
    (Boolean): Is target in lyst?
    """
    mid = len(lyst) // 2

    if len(lyst) == 0:
        return False
    elif lyst[mid] == target:
        return True
    elif lyst[mid] > target:
        return _binary_search(lyst[:mid], target)
    else:
        return _binary_search(lyst[mid+1:len(lyst)], target)


@time_it
def binary_search(lyst, target):
    """
    Recursive helper function for _binary_search().
    Allows for timing the function
    Parameters
    ----------
    lyst : list
        The list to be sorted
    target : int
        The target in the list

    Returns
    -------
    Boolean: Is target in lyst?
    """
    return _binary_search(lyst, target)


def _jump_search(lyst, target):
    """
    Performs a recursive jump search on a list. It works by dividing the list into 10 segments.
    For each segment, perform another jump search if target is within the first and last value.
    Repeat this process until there are not enough values for a jump search; perform a linear search
    on the remaining values.
    The
    Parameters
    ----------
    lyst
    target

    Returns
    -------
    (boolean): Is target in lyst?
    """
    length = len(lyst)  # The length of the list
    jump_length = length // 10  # The jump length. The number of jumps to be performed

    if jump_length == 0:  # If there are not enough items in lyst to perform a jump sort
        # Do a linear search of the values
        for i in lyst:
            if i == target:
                return True
        return False

    previous = 0  # The previous index of the sort
    for i in range(1, 11):
        # The actual jump sorting
        current = i * jump_length  # The current index of the sort
        if current > length - 1:  # If the current index is larger than the actual lyst
            # Perform a jump sort with the last values of lyst
            return _jump_search(lyst[previous:length], target)

        elif lyst[current] == target:  # If the current index is the target
            return True

        elif lyst[current] > target:  # If the current index is LARGER than the target
            # Perform a recursive jump search from the previous index to the current index
            return _jump_search(lyst[previous:current], target)

        # Update the previous index
        previous = current


@time_it
def jump_search(lyst, target):
    """
    A recursive helper function for _jump_search().
    Allows for timing of the function.
    Parameters
    ----------
    lyst : List
        The list to be searched
    target : int
        The target in the lyst

    Returns
    -------
    Boolean: Is target in lyst?
    """
    return _jump_search(lyst, target)


def main():
    """
    The main function for search.py.
    Returns
    -------
    None
    """
    data_size = 1_000_000
    print(data_size)
    lyst = make_data(data_size)
    linear_search(lyst, data_size // 2)
    binary_search(lyst, data_size // 2)
    jump_search(lyst, data_size // 2)


if __name__ == "__main__":
    main()
