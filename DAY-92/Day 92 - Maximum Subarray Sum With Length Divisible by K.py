from typing import List
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        pref = 0
        mem = {0 : 0}            
        ans = float('-inf')

        for i in range(n):
            pref += nums[i]

            R = i + 1
            rem = R % k

            if rem in mem:                
                cur = pref - mem[rem]
                ans = max(ans, cur)
                mem[rem] = min(pref, mem[rem])
            else:
                mem[rem] = pref
        
        return ans