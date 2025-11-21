from collections import Counter
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = set()
        left = set()
        right = Counter(s)
        
        for m in s:
            right[m] -= 1 
            
            for ele in left:
                if right[ele] >= 1:
                    ans.add((ele,m))
            left.add(m)

        return len(ans)