class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.prefix = [[0] * (m + 1) for r in range(n+1)]
        for r in range(n):
            curr = 0
            for c in range(m):
                curr += matrix[r][c] 
                above = self.prefix[r][c+1]
                self.prefix[r+1][c+1] = curr + above 
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1 , row2, col2 = row1+1, col1+1 , row2+1, col2+1
        return self.prefix[row2][col2] - self.prefix[row1-1][col2]  - self.prefix[row2][col1 -1]+ self.prefix[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)