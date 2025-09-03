from typing import List
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)

        
        xs = sorted(set(x for x, y in points))
        ys = sorted(set(y for x, y in points))
        x_map = {x:i+1 for i, x in enumerate(xs)}  
        y_map = {y:i+1 for i, y in enumerate(ys)}

        
        m = len(xs)
        k = len(ys)
        grid = [[0]*(k+2) for _ in range(m+2)]
        for x, y in points:
            grid[x_map[x]][y_map[y]] = 1

        
        ps = [[0]*(k+2) for _ in range(m+2)]
        for i in range(1, m+1):
            for j in range(1, k+1):
                ps[i][j] = (grid[i][j] 
                            + ps[i-1][j] 
                            + ps[i][j-1] 
                            - ps[i-1][j-1])

        def rect_count(x1, y1, x2, y2):
            return (ps[x2][y2] - ps[x1-1][y2] - ps[x2][y1-1] + ps[x1-1][y1-1])

        
        ans = 0
        for i in range(n):
            xa, ya = points[i]
            for j in range(n):
                if i == j: continue
                xb, yb = points[j]

               
                if xa <= xb and ya >= yb:
                    x1, x2 = x_map[xa], x_map[xb]
                    y1, y2 = y_map[yb], y_map[ya]
                    if rect_count(x1, y1, x2, y2) == 2:
                        ans += 1
        return ans
