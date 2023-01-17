# Search for a num in array and return index or if it does not exist return its index if it did 
# array in sorted 

class Solution:
    def searchInsert (self, nums, target: int) -> int:
        # Log(n)
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (1 + r) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid] :
                l = mid + 1

            else:
                r = mid - 1

        return l