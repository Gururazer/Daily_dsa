from typing import List
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums.sort()
        
        ans = sum(nums)
        if ans % 3 == 0:
            return ans

        mod1 = []
        mod2 = []
        for i in nums:
            if i % 3 == 1:
                mod1.append(i)
            elif i % 3 == 2:
                mod2.append(i)
        rm = float('inf')
        if ans % 3 == 1:
            if len(mod1):
                rm = min(mod1[0],rm)
            if len(mod2) > 1:
                rm = min((mod2[0] + mod2[1]),rm)
        else:
            if len(mod2):
                rm = min(rm,mod2[0])
            if len(mod1) > 1:
                rm = min(rm,(mod1[0]+ mod1[1]))
        return ans - rm