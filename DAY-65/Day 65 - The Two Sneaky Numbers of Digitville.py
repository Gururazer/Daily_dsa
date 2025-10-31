from typing import List
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hmp = set()
        res = [] 
        i = 0
        while len(res) < 2:
            
            if nums[i] in hmp:
                res.append(nums[i])
            hmp.add(nums[i])
            i += 1
        return res