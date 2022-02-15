"""
There are people sitting in a circular fashion,
print every third member while removing them,
the next counter starts immediately after the member is removed.
Print till all the members are exhausted.

For example:
Input: consider 123456789 members sitting in a circular fashion,
Output: 369485271
"""


def josephus(int_list, skip):
    skip = skip - 1                     # list starts with 0 index
    idx = 0
    len_list = (len(int_list))
    while len_list > 0:
        idx = (skip + idx) % len_list   # hash index to every 3rd
        yield int_list.pop(idx)
        len_list -= 1


arr = [1,2,3,4,5,6,7,8,9]
arr2 = [1,2,3,4,5,6,7,8,9]

for i in range(len(arr)):
    print(str(next(josephus(arr,3))))

print('Reversing the array: ' + str(arr2[::-1]))