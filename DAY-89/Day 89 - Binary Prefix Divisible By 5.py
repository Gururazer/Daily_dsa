from typing import List
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        c = 0
        
        
        for i in nums:
            
            
            c = (c * 2 + i) % 5
            
            ans.append(c == 0)

        return ans