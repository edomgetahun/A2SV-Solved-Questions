class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # graph = defaultdict(list)
        # for node1, node2 in edges:
        #     graph[node1].append(node2)
        #     graph[node2].append(node1)
        
        # vis = set() 
        # # def dfs(node, vis):         # this code also return when the visted all
        # #     if node == destination:
        # #         return True
        # #     vis.add(node)
        # #     for negh in graph[node]:
        # #         if negh not in vis:
        # #             found = dfs(negh, vis)
        # #             if found :
        # #                 return True
        # #     return False  
        # # return dfs(source, vis)
        # stack = [source]
        # while stack:
        #     node = stack.pop()
        #     if node == destination:
        #         return True
            
        #     if node in vis:
        #         continue 
        #     vis.add(node)
        #     for negh in graph[node]:
        #         if negh not in vis:
        #            stack.append(negh)
        # return False
        graph = [[] for _ in range(n)]
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        vis = set()

        def dfs(node, vis):
            if node == destination:
                return True
            vis.add(node)
            for negh in graph[node]:
                if negh not in vis:
                    found = dfs(negh, vis)
                    if found:
                        return True
            return False
        return dfs(source, vis)

                





