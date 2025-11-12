import math
from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n,n1s,g = len(nums),0,0

        for num in nums:
            if num == 1:
                n1s += 1
            g = math.gcd(g,num)        

        if n1s:
            return n - n1s
        if g > 1:
            return -1

        mlen = n

        for i in range(n):
            g = 0
            for j in range(i, n):
                g = math.gcd(g, nums[j])
                if g == 1:
                    mlen = min(mlen, j - i + 1)
                    break
        return mlen + n - 2