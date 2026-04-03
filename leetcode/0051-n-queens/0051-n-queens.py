class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        left_d = set()
        right_d = set()
        q = []
        temp  = [[0] * n for c in range(n)]
        output = []
        def helper(r):
            # out of bound (we have put n queens)
            if r == n:
                for i in range(n):
                    for j in range(n):
                        if (i,j) in q:
                            temp[i][j] = "Q"
                        else:
                            temp[i][j] = "."
                
                temp2 = []
                for row in range(n):
                    temp2.append("".join(temp[row]))

                output.append(temp2)
                return 
            for c in range(n):
                if c not in col and r-c not in left_d and r+c not in right_d:
                    # put the queen
                    col.add(c)
                    left_d.add(r-c)
                    right_d.add(r+c)
                    q.append((r,c))

                    # go to next row
                    helper(r+1)
                    
                    # remove the queen
                    col.remove(c)
                    left_d.remove(r-c)
                    right_d.remove(r+c)
                    q.pop()
        helper(0)
        return output