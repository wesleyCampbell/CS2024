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


def swap(lyst, first, second):
    """
    Swaps two values in a lyst

    Parameters
    ----------
    lyst : List
        The list where values are being swapped
    first : Int
        The first index to be swapped
    second : Int
        The second index to be swapped

    Returns
    -------
    None
    """
    lyst[first], lyst[second] = lyst[second], lyst[first]


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
        print(f"Starting {func.__name__}")
        result = func(*args, **kwargs)
        end = time.perf_counter()

        print(f"{func.__name__} duration: {end - start} seconds.\n")
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

        # While i pointer is less than the length of the list
        # and the next value is less than the current
        while current_index < len(lyst) - 1 and lyst[current_index + 1] < current_value:
            # Shift the list down
            lyst[current_index] = lyst[current_index + 1]
            current_index += 1
        lyst[current_index] = current_value

    return lyst


def mergesort(lyst):
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


def _merge_sort(lyst, pointer_l, pointer_r):
    """
    Performs the merge sort algorithm on lyst.
    This algorithm is recursive. It does not use
    the Python slice function.

    Parameters
    ----------
    lyst : List
        The list being sorted
    pointer_l : Int
        The pointer for the beginning of the sub-list
    pointer_r : Int
        The pointer for the end of the sub-list

    Returns
    -------
    (List): The sorted list
    """
    # If the pointers are the same, exit recursion
    if pointer_l == pointer_r:
        return [lyst[pointer_l]]

    mid = (pointer_r - pointer_l) // 2 + pointer_l

    left = _merge_sort(lyst, pointer_l, mid)
    right = _merge_sort(lyst, mid + 1, pointer_r)

    return _merge(left, right)


def _merge(list_a, list_b):
    """
    Used in the _merge_sort() function.
    Merges two lists -- a and b -- into one sorted
    list.

    Parameters:
    -----------
    list_a : List
        The first list
    list_b : List
        The second list

    Returns:
    --------
    merged : List
        The merged and sorted list
    """
    i = 0
    j = 0
    merged = []
    # Iterate through both lists.
    # If the value in the first list is
    # Less than that of the second, add it to
    # merged; and vice-versa.
    while i < len(list_a) and j < len(list_b):
        if list_a[i] < list_b[j]:
            merged.append(list_a[i])
            i += 1
        else:
            merged.append(list_b[j])
            j += 1

    # Add the remaining values in the first list to merged
    while i < len(list_a):
        merged.append(list_a[i])
        i += 1

    # Add the remaining values in the second list to merged
    while j < len(list_b):
        merged.append(list_b[j])
        j += 1

    return merged


def quicksort(lyst):
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
    if left < right:
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
    swap(lyst, pivot, right)
    pivot = right

    # The pointer for values less than the pivot
    pointer = left - 1

    # For each value in the list, if the value is less
    # than the pointer, swap it with the pointer
    while left < right:
        if lyst[left] <= lyst[pivot]:
            # Increment the lesser value pointer and swap
            pointer += 1
            swap(lyst, pointer, left)

        # Increment the searching pointer
        left += 1
    # Swap the pivot value with its proper index
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
    # The center index of the list
    mid_index = (right - left) // 2 + left

    first_value = (left, lyst[left])  # The first value in the list
    last_value = (right, lyst[right])  # The second value in the list
    mid_value = (mid_index, lyst[mid_index])  # The middle value of the list

    values = [first_value, last_value, mid_value]

    # Get the median of the three values and return
    median = statistics.median([x[1] for x in values])
    for value in values:
        if value[1] == median:
            return value[0]
    # Gets pylint off my chest (If there is no median return first value)
    return first_value[0]


def timsort(lyst):
    """
    The built-in sorting function in python.
    Combination of merge-sort and selection-sort.

    Paramaters:
    -----------
    lyst : List
        The list to be sorted

    Returns:
    --------
    (list): The sorted list
    """
    return sorted(lyst)


def main():
    """
    The main function for sort.py.
    Times the five search algorithms
        - selection_sort()
        - insertion_sort()
        - mergesort()
        - quicksort()
        - timsort()
    """
    data_size = 50000
    data_gen = make_data(data_size)

    # Selection sort algorithm
    time_it(selection_sort)(next(data_gen))
    # Insertion sort algorithm
    time_it(insertion_sort)(next(data_gen))
    # Merge sort algorithm
    time_it(mergesort)(next(data_gen))
    # Quick sort algorithm
    time_it(quicksort)(next(data_gen))
    # Timsort algorithm
    time_it(timsort)(next(data_gen))


if __name__ == "__main__":
    main()
