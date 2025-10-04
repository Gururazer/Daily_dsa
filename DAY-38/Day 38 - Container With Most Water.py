from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_a = 0
        i = 0
        j = len(height) - 1
        while(i < j):
            h = min(height[i],height[j])
            w = j - i
            area = h * w

            max_a = max(max_a, area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_a
            
