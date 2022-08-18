class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        index = 0
        n = len(nums)
        for i in range(n):
            if nums[i] < target:
                index += 1
        return index
