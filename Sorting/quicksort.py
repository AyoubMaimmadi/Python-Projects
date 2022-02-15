def quick_sort(array):
    """
    Implementation of Quick Sort in Python.
    
    :param array: A array or a list which is supposed to be sorted.
    :return: The same array or list sorted in Ascending order.
    """
    low = 0
    length = len(array)
    high = length - 1

    algorithm(array, low, high)
    return array


def algorithm(sorted_array, low, high): 
    if low >= high:
        return
    else:
        pivot = sorted_array[high]
        left = low
        right = high - 1
        while True:
            while sorted_array[left] < pivot:
                left += 1
            while sorted_array[right] > pivot:
                right -= 1
            if left < right:
                sorted_array[left], sorted_array[right] = sorted_array[right], sorted_array[left]
                left += 1
                right -= 1
            else:
                sorted_array[high], sorted_array[left] = sorted_array[left], sorted_array[high]
                break

        algorithm(sorted_array, low, left - 1)
        algorithm(sorted_array, left + 1, high)


print(quick_sort([8, 2, 1, 6, 3, 4, 9, 7, 5]))
