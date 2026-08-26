class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,elt in enumerate(nums):
            for j,jlt in enumerate(nums):
                if i!=j and elt+jlt == target:
                    return [min(i,j),max(i,j)]
