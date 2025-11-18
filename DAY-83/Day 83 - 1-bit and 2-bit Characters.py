from typing import List
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        if bits[-1] == 1:
            return False
        n = len(bits)
        i = 0
        while i < n:  
            if i == n-1 and bits[i] == 0:
                return True                              
            if i < n and bits[i] == 0:
                i += 1
            while i < n and bits[i] == 1:
                i += 2
            
        return False
    
s = Solution()
s.isOneBitCharacter([1,0,0]) # True
s.isOneBitCharacter([1,1,1,0]) # False