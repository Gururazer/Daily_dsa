from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        dp = [[0] * (n + 1) for _ in range(m+1)]

        freqmp = [[s.count('0'), s.count('1')] for s in strs]

        for zero, one in freqmp:
            for z in range(m, zero - 1, -1):
                for o in range(n, one - 1, -1):
                    dp[z][o] = max(dp[z][o], 1 + dp[z - zero][o - one])
        
        return dp[-1][-1]