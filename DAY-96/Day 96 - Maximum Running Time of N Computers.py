from typing import List
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        l, r, ans = min(batteries), sum(batteries) // n, 0

        while l <= r:
            mid = (l + r + 1) // 2
            reserve = 0
            for b in batteries:
                reserve += min(b, mid)

            if reserve >= mid * n:
                l = mid + 1 
                ans = mid
            else:
                r = mid - 1

        return ans