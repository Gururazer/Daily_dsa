import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        m_hp = []
        for p, t in classes:
            if p == t:
                heapq.heappush(m_hp, (0, p, t))
            else: 
                gain = (p + 1) / (t + 1) - p / t
                heapq.heappush(m_hp, (-gain, p, t))
        
        for i in range(extraStudents):
            n_g, p, t = heapq.heappop(m_hp)

            p += 1
            t += 1
            
            if p == t:
                new_n_g = 0
            else:
                n_g = (p + 1) / (t + 1) - p / t
                new_n_g = -n_g

            heapq.heappush(m_hp, (new_n_g, p, t))
        
        totavg = 0
        for _, p, t in m_hp:
            totavg += p / t 
            
        return totavg / len(classes)