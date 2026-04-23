class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        dir = [(0,1), (0,-1), (1, 0), (-1,0)]
        def inbound(row, col):
            if 0 <= row < n and 0 <= col < m :
                return True
            return False
       
        vis = [[False for i in range(m)] for _ in range(n)]
        def dfs(board, vis , row, col):
            if not inbound(row, col) or vis[row][col] or board[row][col] == "X":
                return 
            
            vis[row][col] = True
            for row_cha, col_cha in dir:
                next_row, next_col = row + row_cha , col + col_cha
                dfs(board, vis, next_row, next_col)
        
        for i in range(n):
            for j in range(m):
                if (i == 0 or j == 0 or i == n-1 or j == m-1) and board[i][j] == "O" :
                    dfs(board, vis, i, j)
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and vis[i][j] == False:
                    board[i][j] = "X"

