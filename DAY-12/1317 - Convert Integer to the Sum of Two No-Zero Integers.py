from typing import List
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        def is_no_zero(num):
            if num == 0:
                return False
            while num > 0:
                if num % 10 == 0:
                    return False
                num //= 10
            return True

        for a in range(1, n):
            b = n - a
            if is_no_zero(a) and is_no_zero(b):
                return [a, b]
        return []