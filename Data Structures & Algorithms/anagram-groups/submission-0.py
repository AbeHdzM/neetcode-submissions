class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        b = {}
        for x in strs:
            sorted_text = "".join(sorted(x))
            if sorted_text in b:
                b[sorted_text].append(x)
            else:
                b[sorted_text] = [x]
        return list(b.values())