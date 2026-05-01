class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}
        for char1 in s:
            if char1 in hash1:
                hash1[char1] = hash1[char1] + 1
            else:
                hash1[char1] = 1
        for char2 in t:
            if char2 in hash2:
                hash2[char2] = hash2[char2] + 1
            else:
                hash2[char2] = 1
        res = True
        if len(hash1) != len(hash2):
            return False
        for e in hash1:
            if e not in hash2 or hash1[e] != hash2[e]:
                return False
        return res
        