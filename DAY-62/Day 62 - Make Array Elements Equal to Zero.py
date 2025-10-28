from typing import List
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        prefixsum = 0
        suffixsum = sum(nums)
        ans = 0

        for x in nums:
            if x == 0:
                if prefixsum == suffixsum:
                    ans += 2
                elif prefixsum -1 == suffixsum or prefixsum == suffixsum - 1:
                    ans += 1
            prefixsum += x
            suffixsum -= x
        
        return ans