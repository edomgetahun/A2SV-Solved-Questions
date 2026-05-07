from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))

    for i in range(n):
        r[i] -= 1

    q = deque()
    incoming = [0] * n
    for num in r:
        incoming[num] += 1

    for i in range(n):
        if incoming[i] == 0:
            q.append(i)

    year = 1
    while q:
        year += 1
        size = len(q)
        for _ in range(size):
            node = q.popleft()
            neigh = r[node]  
            incoming[neigh] -= 1
            if incoming[neigh] == 0:
                q.append(neigh)
    print(year+1)