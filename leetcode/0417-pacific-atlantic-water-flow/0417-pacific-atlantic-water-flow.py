class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        dir = [(0,1), (0,-1),(1,0),(-1,0)]
        pas = set()
        atl = set()
        def inbound(r,c):
            return 0 <= r < n  and 0 <= c < m

        def dfs(r,c, ocean):
            ocean.add((r,c))
            for dr, dc in dir:
                next_r , next_c = r + dr ,c + dc
                if inbound(next_r, next_c) and (next_r, next_c) not in ocean and  heights[next_r][next_c] >= heights[r][c]:
                    dfs(next_r, next_c, ocean)

        for i in range(n): 
            if (i,0) not in pas:
                dfs(i, 0, pas)
        for j in range(m): 
            if (0,j) not in pas:
                dfs(0,j, pas)

        for i in range(n):
            if (i, m-1) not in atl:
                dfs(i, m-1, atl)
        for j in range(m):
            if (n-1, j) not in atl:
                dfs(n-1, j, atl)
        
        res = []
        for i in range(n):
            for j in range(m):
                if (i, j) in pas and (i,j) in atl:
                    res.append([i,j])
        return res