class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
      
    
        points.sort(key=lambda x: (x[0], -x[1]))
        cnt = 0
        n = len(points)
        
        for i in range(n):
            yup = points[i][1]
            ylow = float('-inf')
    
            for j in range(i + 1, n):
                cur_y = points[j][1]
                if cur_y <= yup and cur_y > ylow:
                    cnt += 1
                    ylow = cur_y
                    if cur_y == yup:
                        break
        return cnt  