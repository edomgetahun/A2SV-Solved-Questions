class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = [[] for _ in range(n)]
        incoming = [0] * n
        for pre, course in relations:
            adj[pre-1].append(course-1)
            incoming[course-1] += 1

        q = deque()
        res = [0] * n     
        for i in range(n):
            if incoming[i] == 0:
                q.append(i)
                res[i] = time[i]

        while q:
            node = q.popleft()
            for negh in adj[node]:
                res[negh] = max(res[negh], time[negh] + res[node])
                incoming[negh] -= 1
                if incoming[negh] == 0:
                    q.append(negh)
        return max(res)





            
            