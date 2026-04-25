class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [[] for _ in range(n)]
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, r2 = bombs[j]
                distace_sq =  (x1 - x2) ** 2 + (y1 - y2) ** 2
                if r1 ** 2 >= distace_sq:
                    graph[i].append(j)

        def dfs(i, vis):
            vis[i] = True
            total = 1
            for negh in graph[i]:
                if not vis[negh]:
                    total += dfs(negh, vis)
            return total
        
        res = 0
        for i in range(n):
            vis = [False] * n
            res = max(res, dfs(i, vis))
        return res

        # def dfs(i, vis):
        #     vis.add(i)
        #     for negh in graph[i]:
        #         if negh not in vis:
        #             dfs(negh, vis)
        # res = 0
        # for i in range(n):
        #     vis = set()
        #     dfs(i, vis)
        #     res = max(res, len(vis))
        # return res



                  
    
        
                    
                




                  

