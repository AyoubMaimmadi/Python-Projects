def bubbleSort(arr):
    n = len(arr)
    if n == 0: 
        return False
    for i in range(n):
        for j in range(0, n - 1 - i):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def findKLargest(arr, k):

    n = len(arr)
    if n == 0: 
        return False

    #arr.sort()
    bubbleSort(arr)

    return arr[n - k]


# Max heap
def findKLargest1(arr, k):
    pass




def findKlargest2(arr, k):

    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)


A = [4, 2, 9, 7, 5, 6, 3 ,7, 1, 3]




print(findKLargest(A, 4))
print(findKlargest2(A, 4))



