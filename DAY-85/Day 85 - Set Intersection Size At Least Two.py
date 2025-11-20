from typing import List
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals, key = lambda x : x[1])

        ans = 0
        c = []
        for s,e in intervals:
            if not c or s > c[1]:
                ans += 2
                c = [e-1,e]
            elif s > c[0]:
                ans += 1
                if c[1] == e:
                    c = [e-1,e]
                else:
                    c = [c[1],e]
        return ans                    
