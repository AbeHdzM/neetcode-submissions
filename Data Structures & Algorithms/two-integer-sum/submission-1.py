class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        b = {}
        for i, x in enumerate(nums):
            a = target - x
            if a in b:
                return [b[a], i]
            b[x] = i
