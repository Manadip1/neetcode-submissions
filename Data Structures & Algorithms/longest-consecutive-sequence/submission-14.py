class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        counter = 1
        m = 0
        for i in nums:
            if i-1 not in s:
                n = i+1
                while n in s:
                    s.remove(n)
                    counter += 1
                    n+= 1
                if counter > m:
                    m = counter
            counter = 1
        return m