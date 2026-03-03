from collections import Counter
t = int(input())
for _ in range(t):
    n , k = map(int, input().split())
    c = input()
    
    count = Counter()
    min_ch = float('inf')
    for i in range(k):
        count[c[i]] += 1
    change = count["W"]
    min_ch = change
    
    l = 0
    for r in range(k, len(c)):
        count[c[r]] += 1
        count[c[l]] -= 1
        change = count["W"]
        min_ch = min(min_ch, change)
        l += 1
    print(min_ch)
    


