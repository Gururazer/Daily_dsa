from typing import List
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:        
        n = len(nums)

        i = 0
        while i < n and nums[i] != 1:
            i += 1
        
        j = i + 1
        
        while j < n:
            while j < n and  nums[j] != 1:
                j += 1
            if j < n and (j - i - 1) < k:
                return False    
            i = j
            j = i + 1
        
        return True   