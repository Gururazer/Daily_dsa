from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        m = len(potions)
        pairs = []

        for spell in spells:
            req_str = (success + spell - 1) // spell
            
            k = bisect_left(potions, req_str)
            
            s_cnt = m - k
            pairs.append(s_cnt)
            
        return pairs