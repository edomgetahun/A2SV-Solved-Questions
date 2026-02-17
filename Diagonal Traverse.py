class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        r, c = 0, 0
        res = []

        if not mat or n == 0:
            return [] 
        
        dir = 1  # upright, -1 = bottom left
        for i in range(m * n):
            res.append(mat[r][c])
            if dir == 1:    
                if r == 0 and c != m - 1: 
                    c += 1
                    dir = -1 
                elif c == m -1:
                    r += 1
                    dir = -1
                else:
                    r -= 1
                    c += 1
            else:
                if c == 0 and r != n-1: 
                    r += 1
                    dir = 1
                elif r == n - 1:
                    c += 1
                    dir = 1
                else:
                    r += 1
                    c -= 1
        return res




