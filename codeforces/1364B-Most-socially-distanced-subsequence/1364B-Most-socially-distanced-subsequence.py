t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    if n == 2:
        print(n)
        print(*p)
        continue

    res = []
    res.append(p[0])
    l = 0
    r = 1
    while r < n-1:
        if (p[r] > p[l] and p[r] > p[r+1]) or (p[r] < p[l] and p[r] < p[r+1])  :
            res.append(p[r])
            l = r
        r += 1
    
    if p[n-1] != res[-1]:
        res.append(p[n-1])
    print(len(res))
    print(*res)