t = int(input())
for _ in range(t):
    n , k = map(int, input().split())
    res = []
    for cas in range(n):
        l, r , real = map(int, input().split())
        res.append([l,r,real])
    res.sort()
    
    max_coins = 0
    for cas in res:
        l, r , real = cas
        if l > k or k > r:
            k = max(k, max_coins)
        if l <= k <= r:
            max_coins = max(max_coins, real)   
    print(max(k, max_coins))

        


