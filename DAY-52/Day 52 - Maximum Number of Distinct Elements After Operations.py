from typing import List
from collections import Counter
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        max_dnt = -float('inf')
        nums.sort()
        dcnt = 0
        for num in nums:
            up = num + k
            lw = num - k
            cand = max(max_dnt+1,lw)

            if cand <= up:
                max_dnt = cand  
                dcnt += 1
        return dcnt




s = Solution()
print(s.maxDistinctElements([1,2,2,3,3,4], 2)) # 6

print(s.maxDistinctElements([4,4,4,4], 1)) # 3

print(s.maxDistinctElements([1,1,1,1,1,1,1,1,5,5,5], 3)) # 10

print(s.maxDistinctElements([8,8,10,9,9], 1)) # 5

print(s.maxDistinctElements([7,7,7,7,8,9,8], 2)) # 7
