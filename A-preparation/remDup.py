class Solution :
    def removeDuplicates (self, nums) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums [r] != nums [r - l]:
                nums[l]= nums[r]
                l += 1
        return l