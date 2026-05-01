class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numMap = {}
        for i, num in enumerate(nums):
            if num in numMap:
                return True
            numMap[num] = i
        return False         