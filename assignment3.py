import random
import time
import sys

def randomized_quicksort(arr):
    
    """
    Sorts a list of numbers by selecting a pivot at random to 
    partition the array.

    Args:
        arr (list): A list of unsorted numbers.

    Returns:
        list: A new list containing the fully sorted numbers.
    """

    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + middle + randomized_quicksort(right)

def deterministic_quicksort(arr):

    """
    Sorts a list of numbers by selecting the first element as the pivot
    to partition the array.

    Args:
        arr (list): A list of unsorted numbers.

    Returns:
        list: A new list containing the fully sorted numbers.
    """

    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quicksort(left) + middle + deterministic_quicksort(right)

