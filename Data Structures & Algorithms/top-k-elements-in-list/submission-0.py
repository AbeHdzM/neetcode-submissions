class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        b = {}
        res=[]
        for x in nums:
            if x in b:
                b[x]+=1
            else:
                b[x]=1
        buckets = [[] for _ in range(len(nums)+1)]
        for number, count in b.items():
            buckets[count].append(number)
        for item in reversed(buckets):
            if item:                
                res.extend(item)      
            if len(res) >= k:
                return res[:k]