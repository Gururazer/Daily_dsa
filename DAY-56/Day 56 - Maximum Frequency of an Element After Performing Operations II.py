from typing import List
from collections import Counter
from bisect import bisect_left
from bisect import bisect_right

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()

        potentials = set(nums)
        for x in nums:
            potentials.add(x - k)

        ans = 0

        for tar in sorted(list(potentials)):

            l1 = bisect_left(nums, tar - k)
            r1 = bisect_right(nums, tar + k)

            win1 = r1 - l1

            l2 = bisect_left(nums, tar)
            r2 = bisect_right(nums, tar)
            win2 = r2 - l2

            ops_need = win1 - win2
            can_chg = min(ops_need, numOperations)

            curr = win2 + can_chg
            ans = max(curr, ans)

        return ans





        


s = Solution()
print(s.maxFrequency( nums = [1,4,5], k = 1, numOperations = 2)) #2
print(s.maxFrequency(  nums = [5,11,20,20], k = 5, numOperations = 1)) #2
print(s.maxFrequency(  nums = [705110,63707,171344,149391,88269,895293,240613,840378,644168,622957,516522,718199,542864,505174,285477,291482,973560,346971,592203,93565,334118,542041,879458,319820,809009,120805,805475,38650,815289,759660,282178,134051,747549,333600,893473,766202,880181,253464,40745,90529,150458,675647,677888,278436,502427,858706,917159,460515,157946,994135,437972,49076,154055,630463,509667,306321,85276,942332,502301,683212,554014,354975,789856,420040,292967,811148,168986,557992,396400,740753,497077,778072,745368,64863,392797,911152,137377,561062,704613,895328,165779,745108,662483,485428,854084,933042,238252,324938,721680,798857,87237,65484,513866,410928,364456,706484,460944,645494,309129,550753], k = 106748, numOperations = 68)) 