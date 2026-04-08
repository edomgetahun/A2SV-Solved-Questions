class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
         
        # find the row that the number might exist
        self.falg = False
        top, bot = 0, n-1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:  # if the target value is > the max value in that row 
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                self.falg = True 
                break
        if not self.falg:
            return False
        
        # 2nd binary search on the current row
        row = (top + bot) // 2
        l , r = 0 , m - 1   # use these pointers to iterate over the cols
        while l <= r:
            mid = (l+r) // 2
            if matrix[row][mid] > target :
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        return False





        
        



       



            