class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()
        res = False
        for x in nums:
            if x in a:
                return True
            else:
                a.add(x)
        return res