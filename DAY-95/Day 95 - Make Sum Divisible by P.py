from typing import List
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tot = sum(nums)
        tar = tot % p
        if tar == 0:
            return 0

        mp = {0: -1}
        pref = 0
        res = len(nums)

        for i, x in enumerate(nums):
            pref = (pref + x) % p
            target = (pref - tar) % p
            if target in mp:
                res = min(res, i - mp[target])
            mp[pref] = i

        return res if res < len(nums) else -1