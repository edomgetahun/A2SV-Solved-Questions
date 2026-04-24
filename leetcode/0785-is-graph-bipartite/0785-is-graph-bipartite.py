class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = ["white"] * n 
        def dfs(node):
            for negh in graph[node]:
                if color[negh] == "white":
                    if color[node] == "red":
                        color[negh] = "blue"
                    else:
                        color[negh] = "red"
                    if not dfs(negh):
                        return False 
                elif color[negh] == color[node]:
                    return  False
            return True 
        for node in range(n):
            if color[node] == "white":
                color[node] = "red"   
                if not dfs(node):
                    return False
        return True
