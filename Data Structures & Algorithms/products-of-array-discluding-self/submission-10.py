class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new =[]
        zeros = 0
        if nums[0] == 0:
            total = 1
            zeros += 1
        else:
            total = nums[0]
        for i in nums[1:]:
            if i== 0:
                zeros += 1
                continue
            total *= i
        for j in nums:
            if j ==0 and zeros <2:
                new.append(total)
            elif j==0 :
                new.append(0)
            elif zeros >= 1:
                new.append(0)
            else:
                new.append(total//j)
        return new