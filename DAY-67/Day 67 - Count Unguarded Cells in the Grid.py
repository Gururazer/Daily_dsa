from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        dp = [['y' for _ in range(n)] for _ in range(m)]  
       
        for g in guards:
            dp[g[0]][g[1]] = 'g'

        for w in walls:
            dp[w[0]][w[1]] = 'w'

        
        
        for g in guards:
            row = g[0] 
            col = g[1]    
            # g[0] = 1, g[1] = 1
            left = col - 1
            while left > -1 and dp[row][left] != 'w' and dp[row][left] != 'g':
                dp[row][left] = 'n'
                left -= 1
            right = col+1
            while right < n and dp[row][right] != 'w' and dp[row][right] != 'g':
                dp[row][right] = 'n'
                right += 1


            top = row - 1
            while top > -1 and dp[top][col] != 'w' and dp[top][col] != 'g':
                dp[top][col] = 'n'
                top -= 1

            bottom = row + 1
            while bottom < m and dp[bottom][col] != 'w' and dp[bottom][col] != 'g':
                dp[bottom][col] = 'n'
                bottom += 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if dp[i][j] == 'y':
                    ans += 1 


        return ans 













s = Solution()
print(s.countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]])) # 7