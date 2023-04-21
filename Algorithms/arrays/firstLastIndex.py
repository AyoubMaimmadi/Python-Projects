def firstLastIndex(list, target):

    for i in range(len(list)):
        if list[i] == target:
            start = i
            while i + 1 < len(list) and list[i + 1] == target:
                i += 1
            return [start, i]
    return [-1, -1]


def findStart(arr, target):
    if arr[0] == target:
        return 0
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target and arr[mid - 1] < target:
            return mid
        elif arr[mid] < target: #[1, 3, 3, 3, 3, 3, 3, 5, 7, 8, 9]
            left = mid + 1
        else: 
            right = mid - 1
    return -1

def findEnd(arr, target):
    if arr[-1] == target:
        return (len(arr) - 1)
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target and arr[mid + 1] > target:
            return mid
        elif arr[mid] > target: #[1, 3, 3, 3, 3, 3, 3, 5, 7, 8, 9]
            right = mid - 1
        else: 
            left = mid + 1
    return -1

def findEnd2(arr, target):
    if arr[-1] == target: return len(arr) - 1
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target and arr[mid + 1] > target: return mid
        elif arr[mid] > target: right = mid - 1
        else: left = mid + 1
    return -1


def firstLastIndexBinSearch(arr, target):
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1, -1]
    else: 
        start = findStart(arr, target)
        end = findEnd(arr, target)
        return [start, end]
    return [-1, -1]



A = [1, 3, 3, 3, 3, 3, 3, 5, 7, 8, 9]


print("firstLastIndex -> O(n): " , firstLastIndex(A, 3))
print("firstLastIndexBinSearch -> O(logn): " , firstLastIndexBinSearch(A, 3))

