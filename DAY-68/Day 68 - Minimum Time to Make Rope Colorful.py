from typing import List
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n=len(colors)
        l=0
        ans=0
        for r in range(n):
            if (colors[r]!=colors[l]):
                sameColors=neededTime[l:r]
                ans+=sum(sameColors)-max(sameColors)
                l=r
        ans+=sum(neededTime[l:])-max(neededTime[l:])
        return ans        