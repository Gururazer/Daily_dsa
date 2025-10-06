import heapq
from typing import List

class Solution:
    
    def swimInRisingWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        
        pq = [(grid[0][0], 0, 0)]  
        
        
        visited = set([(0, 0)])
        
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while pq:
            
            t, r, c = heapq.heappop(pq)
            
            
            if r == n - 1 and c == n - 1:
                return t
            
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    
                    
                    new_time = max(t, grid[nr][nc])
                    
        
                    visited.add((nr, nc))
                    heapq.heappush(pq, (new_time, nr, nc))
                    
        
        return -1
    
