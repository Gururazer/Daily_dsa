from typing import List
from collections import Counter
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums) + 1
        i = 0
        j = k
        ans = []
        while j < n:
            c = Counter(nums[i:j])
            tmp = sorted(
                c.items(),
                key = lambda a: (a[1],a[0]),
                reverse=True
            )
            
            t = 0
            for idx,_ in enumerate(tmp):
               if idx == x:
                   break
               t +=  _[0]*_[1]
            

            ans.append(t)
            j += 1
            i += 1

        return ans
s = Solution()
print(s.findXSum(nums = [1,1,2,2,3,4,2,3], k = 6, x = 2))
print(s.findXSum( nums = [3,8,7,8,7,5], k = 2, x = 2))