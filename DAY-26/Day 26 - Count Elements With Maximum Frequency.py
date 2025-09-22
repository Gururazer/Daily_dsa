from collections import Counter
from typing import List
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        cnt = Counter(nums)
        s = sorted(cnt.values())
        cur = s[-1]
        ct = 1
        for _ in range(-2,-len(s)-1,-1):
            if s[_] != cur:
                break
            else:
                ct += 1

        return ct*cur