class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        new = []
        for i in nums:
            if i in d:
                d[i] += 1
            else: 
                d[i] = 1
        for i in d:
            new.append((d[i],i))
        new.sort(reverse = True)
        return list(j for i,j in new[:k])