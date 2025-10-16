from typing import List

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        rem  = [0] * value
        for i in nums:
            rem[i % value] += 1
        res = 0    
        while rem[res % value]:
            rem[res % value] -= 1
            res += 1
            print(res)
        return res
    

s = Solution()
print(s.findSmallestInteger([4,5,7,6,11,12],3))            