import heapq
class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0        
        m = len(heightMap)
        n = len(heightMap[0])                
        min_heap = []
        visited = [[False] * n for _ in range(m)]                
        for j in range(n):
            heapq.heappush(min_heap, (heightMap[0][j], 0, j))
            visited[0][j] = True
            if m > 1:
                heapq.heappush(min_heap, (heightMap[m-1][j], m-1, j))
                visited[m-1][j] = True                
        for i in range(1, m - 1):
            heapq.heappush(min_heap, (heightMap[i][0], i, 0))
            visited[i][0] = True
            if n > 1:
                heapq.heappush(min_heap, (heightMap[i][n-1], i, n-1))
                visited[i][n-1] = True                
        total_water = 0                
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]                
        while min_heap:
            height, r, c = heapq.heappop(min_heap)                    
            for dr, dc in directions:
                nr, nc = r + dr, c + dc                        
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True                            
                    trapped = max(0, height - heightMap[nr][nc])
                    total_water += trapped                            
                    new_height = max(height, heightMap[nr][nc])                            
                    heapq.heappush(min_heap, (new_height, nr, nc))                    
        return total_water
    
