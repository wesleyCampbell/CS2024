"""
This module contains four sorting algorithms:
  - Selection Sort
  - Insertion Sort
  - Merge Sort
  - Quick sort
There is also a timing method as well as testing for python's timsort function.
"""

import time
import random
import statistics


def swap(lyst, a, b):
    """
    Swaps two values in a lyst

    Parameters
    ----------
    lyst : List
        The list where values are being swapped
    a : Int
        The first index to be swapped
    b : Int
        The second index to be swapped

    Returns
    -------
    None
    """
    lyst[a], lyst[b] = lyst[b], lyst[a]


def is_sorted(lyst):
    """
    Tests to see if a list is sorted 
    smallest to largest

    Paramaters
    ----------
    lyst: List
        The list of acending values

    Returns:
    (Boolean): Is the list sorted?
    """
    last_value = lyst[0]
    for i in lyst[1:]:
        # If the current value is greater than the previous
        if i < last_value:
            return False
    return True


def time_it(func):
    """
    A wrapper function for timing functions.

    Parameters:
    -----------
    func : Function
        The function being 'wrapped'

    Returns:
    --------
    wrap : Function
        The function that will time func
    """
    def wrap(*args, **kwargs):
        """
        Times func
        """
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        print(f"{func.__name__} took {end - start} to complete.")
        return result

    return wrap


def make_data(size):
    """
    Makes a global data set

    Paramaters:
    -----------
    size : Int
        The size of the dataset. 
        The range of the dataset will also be 
        -2 * size to 2 * size.

    Yields:
    -------
    data : List
        The dataset
    """
    data = random.sample(range(-size * 2, size * 2), size)
    while True:
        yield data


def selection_sort(lyst):
    """
    Runs the selection sort algorithm
    on a list. Sorts from min to max.
    Parameters
    ----------
    lyst : List
        The list to be sorted

    Returns
    -------
    (List): The sorted list
    """
    for i in range(len(lyst) - 1, 0, -1):  # Decrements as lyst gets sorted
        # i points to the end of the unsorted lyst
        max_index = 0  # The largest value in the unsorted lyst
        for j in range(i + 1):  # Goes through the list up to the pointer i
            if lyst[j] > lyst[max_index]:
                max_index = j

        # Swaps the next largest value with the
        # Right pointer
        swap(lyst, max_index, i)

    return lyst


def insertion_sort(lyst):
    """
    Runs the insertion sorting algorithm on a list. Rather than
    Swapping two values, this algorithm simply shifts the list down.

    Paramaters
    ----------
    lyst: List
        The list to be sorted

    Returns
    -------
    (List): The sorted list
    """
    for i in range(len(lyst) - 2, -1, -1):
        current_value = lyst[i]
        current_index = i

        while current_index < len(lyst) - 1 and lyst[current_index + 1] < current_value:
            lyst[current_index] = lyst[current_index + 1]
            current_index += 1
        lyst[current_index] = current_value

    return lyst


def merge_sort(lyst):
    """
    Recursive helper function for _merge_sort()

    Parameters
    ----------
    lsyt: List
        The list being sorted

    Returns:
    (List): The sorted list
    """
    return _merge_sort(lyst, 0, len(lyst) - 1)


def _merge_sort(lyst, a=-1, b=-1):
    """
    Performs the merge sort algorithm on lyst.
    This algorithm is recursive. It does not use
    the Python slice function.

    Parameters
    ----------
    lyst : List
        The list being sorted

    Returns
    -------
    (List): The sorted list
    """
    # If the pointers are the same, exit recursion
    if a == b:
        return [lyst[a]]

    else:
        mid = (b - a) // 2 + a

        left = _merge_sort(lyst, a, mid)
        right = _merge_sort(lyst, mid + 1, b)

        return _merge(left, right)


def _merge(a, b):
    """
    Used in the _merge_sort() function.
    Merges two lists -- a and b -- into one sorted
    list.

    Parameters:
    -----------
    a : List
        The first list
    b : List
        The second list

    Returns:
    --------
    merged : List
        The merged and sorted list
    """
    i = 0
    j = 0
    merged = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    while i < len(a):
        merged.append(a[i])
        i += 1

    while j < len(b):
        merged.append(b[j])
        j += 1

    return merged


def quick_sort(lyst):
    """
    The recursive helper function for the _quick_sort function.

    Parameters:
    -----------
    lyst : List
        The list to be sorted
    """
    return _quick_sort(lyst, 0, len(lyst) - 1)


def _quick_sort(lyst, left, right):
    """
    The quick sorting algorithm. This algorithm utilizes a divide
    and conquor sorting aproach, meaning that it's
    complexity is O(nlog(n))
    This function mutates lyst

    Parameters:
    -----------
    lyst : List
        The list to be sorted
    left : Int
        The pointer for the left-most value
    right : Int
        The pointer for the right-most value

    Returns:
    --------
    lyst : List
        Returns lyst when done. 
    """
    # If the left and right pointers are equal or have passed
    # one another, exit the function. Serves as the base case.
    if (left < right):
        # Partition the sub-list
        pivot = _partition(lyst, left, right)

        # Sort the lesser section of sub-list
        _quick_sort(lyst, left, pivot - 1)
        # Sort the greater section of sub-list
        _quick_sort(lyst, pivot + 1, right)

    return lyst


def _partition(lyst, left, right):
    """
    Used in the _quick_sort() function.
    Used for selecting a pivot value, then
    making all values less than the pivot to
    the right of the pivot. The values greater 
    than the pivot value go to the right.

    Parameters:
    -----------
    lyst : List
        The list that is being partitioned
    left : Int
        The pointer for the left-most value
    right : Int
        The pointer for the right-most value

    Returns:
    --------
    Pointer : Int
        The index of the pivot value
    """
    # Assign the pivot value
    pivot = _get_pivot(lyst, left, right)

    # The pointer for values less than the pivot
    pointer = left - 1

    # For each value in the list, if the value is less
    # than the pointer, swap it with the pointer
    while left < right:
        if lyst[left] <= lyst[pivot]:
            pointer += 1
            swap(lyst, pointer, left)

        left += 1
    swap(lyst, pointer + 1, right)

    return pointer + 1


def _get_pivot(lyst, left, right):
    """
    Used in _partition() function.
    Gets the pivot value by looking at
    the median of the first value, the
    middle value, and the last value.

    Paramaters:
    -----------
    lyst : List
        The list being partitioned
    left : Int
        The pointer for the left-most value
    right : Int
        The pointer for the right-most value

    Returns:
    --------
    median : Int
        The index of the pivot value 
    """
    mid_index = (right - left) // 2 + left

    first_value = (left, lyst[left])
    last_value = (right, lyst[right])
    mid_value = (mid_index, lyst[mid_index])

    values = [first_value, last_value, mid_value]

    median = statistics.median([x[1] for x in values])

    for value in values:
        if value[1] == median:
            return value[0]


def main():
    """
    The main function for sort.py
    """
    selection = time_it(selection_sort)
    insertion = time_it(insertion_sort)
    merge = time_it(merge_sort)
    quick = time_it(quick_sort)

    data_size = 10000
    data_gen = make_data(data_size)

    for func in [selection, insertion, merge, quick]:
        data = next(data_gen)
        sorted_data = func(data)
        print(f"The data is sorted: {is_sorted(sorted_data)}\n\n")


if __name__ == "__main__":
    main()
