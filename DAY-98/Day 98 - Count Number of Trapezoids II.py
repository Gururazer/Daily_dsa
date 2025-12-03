from math import gcd
from collections import defaultdict
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        td = defaultdict(lambda: defaultdict(int))
        vd = defaultdict(lambda: defaultdict(int))

        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1

                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy

                g = gcd(dx, abs(dy))
                sx = dx // g
                sy = dy // g

                de = sx * y1 - sy * x1

                key1 = (sx << 12) | (sy + 2000)
                key2 = (dx << 12) | (dy + 2000)

                td[key1][de] += 1
                vd[key2][de] += 1

        return self.count(td) - self.count(vd) // 2

    def count(self, mp):
        ans = 0

        for inn in mp.values():
            tot = sum(inn.values())
            rem = tot

            for val in inn.values():
                rem -= val
                ans += val * rem

        return ans