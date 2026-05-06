from collections import deque
n = int(input())
names = []
for _ in range(n):
    names.append(input().strip())

adj = [[] for _ in range(26)]
incoming = [0] * 26
for i in range(n-1):
    first = names[i]
    sec = names[i+1]
    diff = False
    for j in range(min(len(first), len(sec))):
        if first[j] != sec[j]:
            u = ord(first[j]) - ord('a')
            v = ord(sec[j]) - ord('a')
            
            if v not in adj[u]:
                adj[u].append(v)
                incoming[v] += 1
            diff = True
            break
    
    if not diff and len(first) > len(sec):
        print("Impossible")
        exit()
    
q = deque()
for i in range(26):
    if incoming[i] == 0:
        q.append(i)

ans = []
while q:
    node = q.popleft()
    ans.append(chr(node + ord('a')))
    for negh in adj[node]:
        incoming[negh] -= 1
        if incoming[negh] == 0:
            q.append(negh)
if len(ans) != 26:
    print("Impossible")
else:
    print("".join(ans))