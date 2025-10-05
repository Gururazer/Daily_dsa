from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        
        pacific_reachable = set()
        atlantic_reachable = set()

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r: int, c: int, reachable_set: set):
            if (r, c) in reachable_set:
                return
            
            reachable_set.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    if heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, reachable_set)

        for r in range(m):
            dfs(r, 0, pacific_reachable)
        for c in range(n):
            dfs(0, c, pacific_reachable)

        for r in range(m):
            dfs(r, n - 1, atlantic_reachable)
        for c in range(n):
            dfs(m - 1, c, atlantic_reachable)

        result = []
        for r in range(m):
            for c in range(n):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    result.append([r, c])
        
        return result