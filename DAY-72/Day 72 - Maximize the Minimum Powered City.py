from itertools import accumulate
from typing import List

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        POWER = [0] * (n + 5)
        

        for i, j in enumerate(stations):
            POWER[max(0, i - r)] += j
            POWER[min(n - 1, i + r) + 1] -= j
        

        lo, hi = min(accumulate(POWER[:n])), 2 * 10**10

        def check(mid):
            df = POWER[:] 
            cur, cnt = 0, 0
            for i in range(n):
                cur += df[i]
                if cur < mid:
                    need = mid - cur
                    cnt += need
                    if cnt > k:
                        return False
                    cur = mid

                    df[min(n - 1, i + 2 * r) + 1] -= need
            return True


        while lo < hi:
            mid = (lo + hi + 1) >> 1
            if check(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo