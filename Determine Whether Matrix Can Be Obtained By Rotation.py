class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        def rotate(mat):
            rotated = [[0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    rotated[c][n-1-r] = mat[r][c]
            return rotated
        
        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)
        return False


                     
