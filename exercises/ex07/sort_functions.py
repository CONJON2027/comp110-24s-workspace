"""Functions that implement sorting algorithms."""

__author__ = ""

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    for i in range(len(x)):
        min_index = i
        for j in range(i+1, len(x)):
            if x[j] < x[min_index]:
                min_index = j
        if min_index != i:
            value = x[i]
            x[i] = x[min_index]
            x[min_index] = value
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    for i in range(len(x)):
        current_min_index = i
        for j in range(i+1, len(x)):
            if x[j] < x[current_min_index]:
                current_min_index = j
        value = x[i]
        x[i] = x[current_min_index]
        x[current_min_index] = value
    return None

