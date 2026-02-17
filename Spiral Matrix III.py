class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        r, c = rStart, cStart
        res.append([r,c])
        
        step = 1
        while len(res) < rows * cols:
            # right
            for _ in range(step):
                c += 1
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r,c])
            # down 
            for _ in range(step):
                r += 1
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r,c])
            step += 1

            #left
            for _ in range(step):
                c -= 1
                if 0 <= r < rows and 0  <= c < cols:
                    res.append([r,c])
            # up 
            for _ in range(step):
                r -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r,c])
            step += 1
        return res
        







        



        
