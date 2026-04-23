class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[False for i in range(m)] for j in range(n)]
        dir = [(0,1), (0,-1), (1, 0), (-1,0)]
        def inbound(row, col):
            if 0 <= row < n and 0 <= col < m:
                return True
            return False 
        def dfs(grid, vis, row, col):
            vis[row][col] = True
            per = 0
            for row_change, col_change  in dir:
                new_row = row + row_change
                new_col = col + col_change

                if not inbound(new_row, new_col):
                    per += 1
                elif grid[new_row][new_col] == 0:
                    per += 1
                elif not vis[new_row][new_col]:
                    per += dfs(grid, vis, new_row, new_col)   
            return per
                    
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return  dfs(grid, vis, i, j)


       