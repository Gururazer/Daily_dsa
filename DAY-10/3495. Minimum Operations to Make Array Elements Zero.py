from typing import List
class solution:
    def get(self, num: int) -> int:
        if num == 0:
            return 0
        result = 0
        k = 1
        i = 1
        while True:
            l = 1 << (i - 1) * 2
            r = (1 << i * 2) - 1
            if l > num:
                break
            count = min(r, num) - l + 1
            result += count * k

            k += 1
            i += 1
        return result

    def minOperations(self, queries: List[List[int]]) -> int:
        result = 0
        for q in queries:
            tot_red = self.get(q[1]) - self.get(q[0] - 1)
            result += (tot_red + 1) // 2
        return result