class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        arr = 1
        end = points[0][1]
        for start, fin in points[1:]:
            if start > end:
                arr += 1
                end = fin
        return arr

                

                
                


