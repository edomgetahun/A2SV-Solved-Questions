from collections import Counter
n, k = map(int, input().split())
a = list(map(int, input().split()))
l = 0
length = 0
count = Counter()
best_l, best_r = 0, 0

for r in range(n):
    count[a[r]] += 1
    while len(count) > k:
        count[a[l]] -= 1
        if count[a[l]] == 0:
            del count[a[l]]
        l += 1
    if r-l+1 > length:
        length = r-l+1
        best_l = l
        best_r = r
print(best_l+1, best_r+1)
        

