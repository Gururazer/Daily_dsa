from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:        
        n = len(nums)        
        forward = [1] * n
        for i in range(1, n):
            if nums[i-1] < nums[i]:
                forward[i] = forward[i-1] + 1
                              
        backward = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i+1]:
                backward[i] = backward[i+1] + 1
                      
        max_k = 1
               
        for j in range(1, n):       
            k1 = forward[j-1]       
            k2 = backward[j]                   
            currk = min(k1, k2)            
            max_k = max(max_k, currk)
            
        return max_k


s = Solution()
print(s.maxIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1])) #3
print(s.maxIncreasingSubarrays([5,8,-2,-1])) #2