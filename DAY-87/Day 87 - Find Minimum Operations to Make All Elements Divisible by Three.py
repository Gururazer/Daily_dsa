from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
            ans = 0
            
            def chk(i: int) -> bool:
                if i % 3 == 0:
                    return True
                return False
            
            for i in nums:
                if chk(i):
                    continue
                if chk(i-1) or chk(i+1):
                    ans += 1
            
            return ans