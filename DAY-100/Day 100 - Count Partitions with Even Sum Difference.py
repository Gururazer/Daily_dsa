from typing import List
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        pospart = 0
        pref = []
        pref.append(0)
        def isparteven(s1: int, s2: int) -> bool:
            return (s1 -s2) % 2 == 0
        
        for i in range(n):
            pref.append(pref[i] + nums[i])
        
        for i in range(n-1):
            if isparteven(pref[i+1],pref[-1] - pref[i+1]):
                pospart += 1 
        return pospart
    
s = Solution()
print(s.countPartitions(nums = [10,10,3,7,6]))