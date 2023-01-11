def containsDup(list): 
    hashset = set()
    
    for n in list:
        if n in hashset:
            return True
        hashset.add(n)
        # print(hashset)
    return False

nums = [1,2,3,4,5,6,7,6]

print(containsDup(nums))