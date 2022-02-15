def heap_sort(array):
    '''
    Implementation of Heap Sort in Python.

    :param array: A array or a list which is supposed to be sorted.
    :return: The same array or list sorted in Ascending order.e
    '''
    length = len(array)

    for item in range(length, -1, -1):
        heapify(array, item, length)
    for count in range(length - 1, 0, -1):
        array[count], array[0] = array[0], array[count]
        heapify(array, 0, count)
    return array


def heapify(sorted_array, element, length):
    largest = element
    left = 2 * element + 1
    right = 2 * element + 2

    if left < length and sorted_array[largest] < sorted_array[left]:
        largest = left
    if right < length and sorted_array[largest] < sorted_array[right]:
        largest = right
    if largest != element:
        sorted_array[largest], sorted_array[element] = sorted_array[element], sorted_array[largest]
        heapify(sorted_array, largest, length)
