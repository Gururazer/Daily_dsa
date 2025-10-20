from typing import List
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        cnt = 0
        for _ in operations:
            if _[1] == '-':
                cnt -= 1
            else:
                cnt += 1
        return cnt
    
s = Solution()
print(s.finalValueAfterOperations(["--X","X++","X++"])) #1