import collections
from bisect import bisect_right

class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:
        n = len(rains)
        ans = [0] * n         
        lrd = collections.defaultdict(int)
        dry_d = []
        for i in range(n):
            lake = rains[i]            
            if lake > 0:                
                ans[i] = -1                
                if lake in lrd:                
                    prd = lrd[lake]                                        
                    idx = bisect_right(dry_d, prd)                    
                    if idx < len(dry_d):                
                        ddi = dry_d[idx]                                        
                        ans[ddi] = lake                                        
                        dry_d.pop(idx)
                    else:                
                        return []                                
                lrd[lake] = i                
            else:                
                dry_d.append(i)                
                ans[i] = 0        
        for i in dry_d:
            ans[i] = 1             
        return ans