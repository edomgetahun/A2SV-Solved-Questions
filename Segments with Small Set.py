from collections import Counter
n, k = map(int, input().split())
a = list(map(int, input().split()))

l = 0
cnt = 0
unique = Counter()
for r in range(n):
    unique[a[r]] += 1
    while len(unique) > k:
        unique[a[l]] -= 1
        if unique[a[l]] == 0:
            del unique[a[l]] 
        l += 1
    cnt += r - l + 1
print(cnt)

