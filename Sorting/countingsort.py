def counting_sort(array):
    """
    Implementation of Counting Sort Sort in Python.

    :param array: A array or a list which is supposed to be sorted.
    :return: The same array or list sorted in Ascending order.
    """
    low = min(array)
    length = len(array)
    if low < 0:
        extra = abs(low)
        array = [element + extra for element in array]

    high = max(array)
    count_array = [0] * (high + 1)

    for item in array:
        count_array[item] += 1

    for index in range(1, len(count_array)):
        count_array[index] += count_array[index - 1]

    sorted_array = [0] * length

    for element in array:
        sorted_array[count_array[element] - 1] = element
        count_array[element] -= 1

    if low < 0:
        sorted_array = [element - extra for element in sorted_array]

    return sorted_array
