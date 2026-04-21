class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        n, m = len(grid) , len(grid[0])
        vis = [[False for i in range(m)] for _ in range(n)]
        dir =  [(0,1), (0,-1), (1, 0), (-1,0)]
        def inbound(row, col):
            if 0 <= row < n and 0 <= col < m:
                return True
            return False
        
        def dfs(grid, vis, row, col):
            if not inbound(row, col) or vis[row][col] == True or grid[row][col] == "0":
                return
            
            vis[row][col] = True
            for row_change, col_change in dir:
                new_row, new_col = row + row_change, col + col_change
                dfs(grid, vis, new_row, new_col)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not vis[i][j]:
                    island += 1
                    dfs(grid, vis, i, j)
        return island