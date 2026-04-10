import bisect
t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
 
    b.sort()
    prev = float('-inf')
    flag = True
    
    for i in range(n):
        keep = float("inf")
        if a[i] >= prev:
            keep = a[i]
        else:
            keep = float('inf')
        # we want b[j] >= prev + a[i] (but we don't know the least possible index so do BS) this derived from  b[j] - a[i] >= prev
        need = prev + a[i]
        indx = bisect.bisect_left(b, need) 
 
        if indx < m:
            op = b[indx] - a[i]
        else:
            op = float('inf')
 
        best = min(keep, op)
        if best == float('inf'):
            flag = False
            break
        
        prev = best
    print('YES' if flag else "NO")