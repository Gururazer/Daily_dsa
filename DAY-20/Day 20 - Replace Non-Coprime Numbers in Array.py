from typing import List
import math
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            current_num = num
            while stack:
                top = stack[-1]
                gcd = math.gcd(top, current_num)
                if gcd > 1:
                    lcm = (top * current_num) // gcd
                    stack.pop()
                    current_num = lcm
                else:
                    break
            stack.append(current_num)
        return stack