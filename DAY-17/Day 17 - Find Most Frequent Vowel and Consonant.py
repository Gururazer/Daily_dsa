from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        VOW = 'aeiou'
        cnt = Counter(s)
        maxv = 0
        maxc = 0
        for _ in cnt.elements():
            if _ in VOW:
                if maxv < cnt[_]:
                    maxv = cnt[_]
            else:
                if maxc < cnt[_]:
                    maxc = cnt[_]
        return maxv + maxc
        

