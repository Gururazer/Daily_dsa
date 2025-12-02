from typing import List
from collections import defaultdict
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        ans = 0

        def posible(n):
            return (n * (n - 1)) // 2
        
        #group by y 
        ymp = defaultdict(int)
        for _,y in points:
            ymp[y] += 1
              

        if len(ymp) < 2:
            return 0
        
        pref = []
        posx = []
        tmp = 0
        for k in sorted(list(ymp.keys())):
            n = posible(ymp[k])
            posx.append(n)
            
            tmp += n
            pref.append(tmp)
        
        
        
        for i in range(len(posx)-1):
            ans += posx[i] * (pref[-1] - pref[i])
            
        
        return ans % MOD