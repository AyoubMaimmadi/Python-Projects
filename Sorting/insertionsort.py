def insertion_sort(array):
    """Implementation of Insertion Sort in Python.

    :param array: A array or a list which is supposed to be sorted.
    :return: The same array or list sorted in Ascending order.
    """
    length = len(array)
    for index in range(1, length):
        key = array[index]
        for sub_index in range(index - 1, -1, -1):
            if key < array[sub_index]:
                array[sub_index + 1] = array[sub_index]
            else:
                array[sub_index + 1] = key
                break
    return array

