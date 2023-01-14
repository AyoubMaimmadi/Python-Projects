nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]

def containerArea(list): 
    res = 0 #result 
    l, r = 0, len(list)-1

    while l < r:
        area = (r - l) * min(list[r], list[l])
        res = max(res, area)
        if list[r] > list[l]:
            l += 1
        else: 
            r -= 1
    return res
        
print(containerArea(nums))
        
