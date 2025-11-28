from collections import defaultdict,deque
from typing import List
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n <= 1 : 
            return 1
        
        count = 0

        
        G = defaultdict(set)
        for u,v in edges: 
            G[u].add(v), G[v].add(u)
        
        
        Q = deque(u for u, vs in G.items() if len(vs) == 1)
        
        
        while Q:
            for _ in range(len(Q)):
                u = Q.popleft()
                
                
                p = next(iter(G[u])) if G[u] else -1
                if p >= 0 : 
                    G[p].remove(u)
                
                
                if values[u] % k == 0: 
                    count += 1
                else: 
                    values[p] += values[u]

                
                if p >= 0 and len(G[p]) == 1: 
                    Q.append(p)

        return count