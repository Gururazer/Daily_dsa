from typing import List
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            newnums = [0] * (len(nums) - 1)
            for i in range(-1,-len(nums),-1):
                newnums[i] = (nums[i] + nums[i-1]) % 10
            nums = newnums    
            return self.triangularSum(nums)

s = Solution()
print(s.triangularSum([1,2,3,4,5])) #8
print(s.triangularSum([5])) # 5