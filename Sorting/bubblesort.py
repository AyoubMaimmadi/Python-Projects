def bubble_sort(array):
    """Implementation of Bubble Sort in Python.
    Bubble sort's time complexities varies as mentioned below :
        --->Best case time complexity :- O(n).
        --->Average case time complexity :- O(n^2).
        --->Worst case time complexity :- O(n^2).
    Bubble sort's Auxiliary space complexity : O(1).

    :param array: A array or a list which is supposed to be sorted.
    :return: The same array or list sorted in Ascending order.
    """

    length = len(array)

    # Traversing through every element of the array instead of first element because it automatically is sorted.
    for cycle in range(length - 1):
        swapped = False

        # Last elements(last cycle number of elements) are already sorted so are not traversed again.
        for index in range(length - cycle - 1):

            # Swap if the element is greater than the next element
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                swapped = True

        # If no swapping is performed than break out of the loop.
        if not swapped:
            break

    return array
