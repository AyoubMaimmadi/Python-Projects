def selection_sort(array):
    """Implementation of Selection Sort in Python.

    :param array: A array or a list which is supposed to be sorted.
    :return: The same array or list sorted in Ascending order.
    """
    length = len(array)
    for index in range(length - 1):
        lowest_value_index = 0
        for sub_index in range(index, length):
            if array[lowest_value_index] > array[sub_index]:
                lowest_value_index = sub_index
        array[index], array[lowest_value_index] = array[lowest_value_index], array[index]
    return array
