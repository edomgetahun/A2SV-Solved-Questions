class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegre = [0 for _ in range(n)] 
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            indegre[b] += 1
        
        q = deque()
        my_dict = defaultdict(set)
        for i in range(n):
            if indegre[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            for child in graph[node]:
                my_dict[child].update(my_dict[node])
                my_dict[child].add(node)
                indegre[child] -= 1
                if indegre[child] == 0:
                    q.append(child)

        res = [[]  for _ in range(n)]
        for key in my_dict:
            res[key] = sorted(list(my_dict[key]))

        return res            




        
 
        
        
