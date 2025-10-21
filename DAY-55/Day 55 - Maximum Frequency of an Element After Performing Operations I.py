from typing import List
from collections import Counter
from bisect import bisect_left
from bisect import bisect_right

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums = sorted(nums)
        cnt = Counter(nums)

        ans = 0

        for n in range(nums[0], nums[-1] + 1):
            left = bisect_left(nums, n - k)
            right = bisect_right(nums, n + k)

            win = right - left

            initial = cnt[n]
            after = min(win - initial, numOperations)

            ans = max(initial + after, ans)

        return ans





        


s = Solution()
print(s.maxFrequency( nums = [1,4,5], k = 1, numOperations = 2)) #2
print(s.maxFrequency(  nums = [5,11,20,20], k = 5, numOperations = 1)) #2