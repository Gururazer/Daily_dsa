from typing import List
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
        dp = [[[-1] * k for j in range(C)] for i in range(R)]

        MOD = 10**9 + 7

        def dfs(r, c, rem):
            if r == R-1 and c == C-1:
                rem = (rem + grid[r][c]) % k
                return 0 if rem else 1
            if r == R or c == C:
                return 0
            if dp[r][c][rem] > -1:
                return dp[r][c][rem]
            dp[r][c][rem] = (
                dfs(r+1, c, (rem + grid[r][c]) % k) % MOD +
                dfs(r, c+1, (rem + grid[r][c]) % k) % MOD
            ) % MOD
            return dp[r][c][rem]

        return dfs(0, 0, 0)