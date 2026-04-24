class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        temp = []
        def dfs(node):
            temp.append(node)
            if node == n-1:
                res.append(temp[:]) 
            else:
                for negh in graph[node]:
                    dfs(negh)
            temp.pop()
        dfs(0)
        return res