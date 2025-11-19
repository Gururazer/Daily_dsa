from typing import List
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        
        def bi(arr: List, tar: int)-> int:
            l = 0
            r = len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] == tar:
                    return tar * 2
                elif arr[mid] < tar:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        
        ans = original
        while original != -1:
            ans = original
            original = bi(nums,original)

        return ans                
s = Solution()
print(s.findFinalValue([5,3,6,1,12],3))    #24