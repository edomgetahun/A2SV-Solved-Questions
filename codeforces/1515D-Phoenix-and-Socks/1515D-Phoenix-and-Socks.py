from collections import Counter
t = int(input())
for _ in range(t):
    n, l , r = map(int, input().split())
    a = list(map(int, input().split()))
    
    left = a[:l]
    right = a[l:]
    countL = Counter(left)
    countR = Counter(right)
    
    for c in list(countL.keys()):
        common = min(countL[c], countR[c])
        countL[c] -= common
        countR[c] -= common
        l -= common
        r -= common

    if l < r:
        countL, countR = countR, countL
        l, r = r, l

    cost = 0
    diff = l - r    
    for c in countL:
        pairs = countL[c] // 2   
        use = min(pairs, diff//2) 
        cost += use
        countL[c] -= use * 2
        diff -= use * 2

    cost += diff //2   # fix the imbalance
    remain = sum(countL.values()) + sum(countR.values())
    cost += remain // 2     # recolor  the remaining
    print(cost)