class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0]) 
        temp = []
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    temp.append([i,j])
            
        
        for indx in temp:
            i, j = indx

            # to the left
            j = j-1 
            while j >= 0:
                matrix[i][j] = 0
                j -= 1
            
            
            # to the right
            i, j = indx
            j = j+1
            while j < c:
                matrix[i][j] = 0
                j += 1
            
            # up
            i, j = indx
            i = i-1
            while i>= 0:
                matrix[i][j] = 0
                i -= 1
            
            # down
            i, j = indx 
            i = i+1
            while i < r:
                matrix[i][j] = 0
                i += 1
        return matrix           
                




