def mergeTwoSortedLists(list1, list2):
    merged_list = []
    merged_list.extend(list1)
    merged_list.extend(list2)
    merged_list.sort()
    merged_list.reverse()
    return merged_list


def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list += list1[i:] + list2[j:]
    return merged_list

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

print(mergeTwoSortedLists(list1, list2))
print(merge_sorted_lists(list1, list2))