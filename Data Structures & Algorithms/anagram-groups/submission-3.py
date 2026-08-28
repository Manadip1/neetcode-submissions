class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        s = set([])
        for i in strs:
            j = sorted(i)
            j = str(j)
            if j in d:
                d[j].append(i)
            else:
                d[j] = [i]
        return list(d.values())