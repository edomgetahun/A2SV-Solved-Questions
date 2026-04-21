class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = ["white"] * n
        res = True
        def dfs(node):
            nonlocal res
            for negh in graph[node]:
                if color[negh] == "white":
                    if color[node] == "red":
                        color[negh] = "blue"
                    else:
                        color[negh] = "red"
                    dfs(negh)
                else:
                    if color[negh] == color[node]:
                        res = False
                        return # stop dfs immediatly
        
        for node in range(n):
            if color[node] == "white":
                color[node] = "red" # start with red
                dfs(node)
                if res == False:
                    break
        return res
