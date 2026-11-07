import random
import time
import sys

# Increases recursion limit since deterministic version hits extreme worst-case depths on the sorted arrays.
sys.setrecursionlimit(2000)

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


# Generate test arrays (Size: 1000)
random_array = [random.randint(0, 1000) for _ in range(1000)]
sorted_array = list(range(1000))
reverse_sorted_array = sorted_array.copy()
reverse_sorted_array.sort(reverse=True)
repeated_array = [random.randint(1, 5) for _ in range(1000)]

arrays = {
    "Random": random_array,
    "Sorted": sorted_array,
    "Reverse Sorted": reverse_sorted_array,
    "Repeated": repeated_array
}

for name, arr in arrays.items():
    print(f"--- {name} Array ---")
    
    start = time.time()
    randomized_quicksort(arr.copy())
    print(f"Randomized: {time.time() - start:.5f} seconds")
    
    start = time.time()
    deterministic_quicksort(arr.copy())
    print(f"Deterministic: {time.time() - start:.5f} seconds\n")

