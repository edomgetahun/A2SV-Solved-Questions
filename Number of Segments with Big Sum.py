n , s = map(int, input().split())
a = list(map(int, input().split()))
curr = 0
res = 0
l = 0
for r in range(n):
    curr += a[r]
    while curr >= s:
        res += n - r
        curr -= a[l]
        l += 1
print(res)

