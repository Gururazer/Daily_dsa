from typing import List
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        n = n+1
        d = [[0] * n for _ in range(n)]

        for q in queries:
            x1 = q[0]
            y1 = q[1]
            x2 = q[2]
            y2 = q[3]

            d[x1][y1] += 1
            d[x1][y2+1] -= 1
            d[x2+1][y1] -= 1
            d[x2+1][y2+1] += 1
        n = n-1
        mat = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                left = mat[i][j-1] if j > 0 else 0
                above = mat[i-1][j] if i > 0 else 0
                diag = mat[i-1][j-1] if i > 0 and j > 0 else 0
                mat[i][j] = d[i][j] + left + above - diag


        return mat