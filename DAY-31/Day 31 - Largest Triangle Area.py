from typing import List
import math
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxarea = 0
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                for k in range(j+1,len(points)):
                    A = self.area(points[i],points[j],points[k])
                    if maxarea < A:
                       maxarea = A
        return maxarea

    def area(self, a : int, b : int, c : int) -> float:
        x1,x2,x3 = a[0],b[0],c[0]
        y1,y2,y3 = a[1],b[1],c[1]
        ar = (1/2)*math.fabs((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)) )
        return ar                
