from typing import List
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for _ in range(len(nums)-(2*k)+1):
            flag1 = False
            flag2 = False    
            for i in range(_,_+k-1):
                if nums[i] >= nums[i+1]:
                   break
                if i == _+k-2:
                   flag1 = True 
            if not (flag1): 
               continue 
            for j in range(_+k,_+(2*k)-1):
                if nums[j] >= nums[j+1]:
                   break
                if j == _+(2*k)-2:
                   flag2 = True 
            if flag1 and flag2:
                return True
        
        return False 

s = Solution()
print(s.hasIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1],3)) #  True
print(s.hasIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7],5)) #  False
print(s.hasIncreasingSubarrays([6,13,-17,-20,2],2)) #  False