from typing import List
from collections import Counter
from bisect import bisect_right
from functools import cache
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        power = sorted(cnt.keys())  
        @cache
        def dp(i):
            if i >= len(power):
                return 0
            leave = dp(i + 1)
            take = bisect_right(power, power[i] + 2)
            return max(leave, cnt[power[i]] * power[i] + dp(take))
        return dp(0)

s = Solution()
print(s.maximumTotalDamage([1,1,3,4])) # 6
print(s.maximumTotalDamage([7,1,6,6])) # 13